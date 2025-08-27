from flask import Flask, request, jsonify, send_file, redirect, render_template_string
import uuid
import pyqrcode
import os
from urllib.parse import urlencode, quote_plus

UPI_ID = "8178535418@slc"
PAYEE_NAME = "HARSH VASHISHTHA"
PORT = 8080

ITEMS = {
    "Center Fresh": 1,
    "Advance": 10,
    "Danish Bhai": 20
}
transactions = {}
os.makedirs("static/qr", exist_ok = True)
 
app = Flask(__name__, static_folder ="static")

SHOP_HTML = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <title> Simple UPI Payments</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial; background:#f7f7fb; margin:0; padding:24px; }
    h1 { margin: 0 0 16px; }
    .grid { display:grid; grid-template-columns: repeat(auto-fit,minmax(220px,1fr)); gap:16px; }
    .card { background:#fff; border-radius:14px; padding:16px; box-shadow:0 10px 25px rgba(0,0,0,.05); }
    .price { font-weight:700; margin:8px 0 16px; }
    button { padding:10px 14px; border:0; border-radius:10px; cursor:pointer; font-weight:600; }
    .primary { background:#2e7d32; color:#fff; }
    .primary:disabled { opacity:.6; cursor:not-allowed; }
    .panel { margin-top:24px; background:#fff; border-radius:14px; padding:16px; box-shadow:0 10px 25px rgba(0,0,0,.05); }
    .row { display:flex; gap:16px; align-items:center; flex-wrap:wrap; }
    img { max-width:220px; height:auto; border:1px solid #eee; border-radius:10px; }
    a { word-break:break-all; }
    .muted { color:#666; font-size:14px; }
  </style>
</head>
<body>
  <h1> Select an item to pay</h1>
  <div class="grid">
    {% for name, price in items.items() %}
      <div class="card">
        <div class="title"><strong>{{ name }}</strong></div>
        <div class="price">₹ {{ price }}</div>
        <button class="primary" onclick="pay('{{ name }}')" id="btn-{{ name|replace(' ','-') }}">Generate UPI</button>
      </div>
    {% endfor %}
  </div>

  <div id="result" class="panel" style="display:none">
    <div class="row">
      <img id="qr" alt="UPI QR" />
      <div>
        <div><strong id="item"></strong></div>
        <div class="muted" id="amount"></div>
        <p><a id="link" href="#" target="_blank">Open in UPI app</a></p>
        <div class="muted" id="tid"></div>
      </div>
    </div>
  </div>

  <script>
    async function pay(item) {
      const btn = document.getElementById('btn-'+item.replaceAll(' ','-'));
      btn.disabled = true;
      try {
        const res = await fetch('/pay_upi', {
          method:'POST',
          headers:{'Content-Type':'application/json'},
          body: JSON.stringify({ item })
        });
        const data = await res.json();
        if (!res.ok) { alert(data.message || 'Failed'); return; }
        // Fill UI
        document.getElementById('result').style.display = 'block';
        document.getElementById('item').textContent   = 'Item: ' + data.item;
        document.getElementById('amount').textContent = 'Amount: ₹ ' + data.amount;
        document.getElementById('tid').textContent    = 'Transaction ID: ' + data.transaction_id;
        document.getElementById('link').href          = data.upi_link;
        document.getElementById('qr').src             = data.qr_code; // it’s already a relative URL like /qr/<id>
      } catch(e) {
        alert('Network error');
      } finally {
        btn.disabled = false;
      }
    }
  </script>
</body>
</html>
"""

@app.route('/')
def home():
    return redirect("/shop")

@app.route("/shop")
def shop():
    return render_template_string(SHOP_HTML,items = ITEMS)

@app.route('/items', methods=['GET'])
def items():
    return jsonify(ITEMS)

@app.route('/pay_upi', methods=['POST'])
def pay_upi():
    data = request.get_json(silent=True)or{}
    item = data.get('item')

    if item not in ITEMS:
        return jsonify({"status": "error", "message": "INVALID ITEM SELECTED!!..."}), 400

    amount = ITEMS[item]

    params = {
        "pa":UPI_ID,
        "PN":PAYEE_NAME,
        "am":f"{amount:2f}",
        "cu":"INR",
        "tn":f"Payment for {item}",
        "tr": str(uuid.uuid4())
    }
        
    upi_link = "upi://pay?" + urlencode(params, quote_via=quote_plus)
    transaction_id = str(uuid.uuid4())

    

    qr_path = os.path.join("static","qr", f"{transaction_id}.png")
    qr = pyqrcode.create(upi_link)
    qr.png(qr_path, scale=6)

    transactions[transaction_id] = {
        "upi_id": UPI_ID,
        "item": item,
        "amount": amount,
        "status": "pending",
        "upi_link": upi_link,
        "qr_file": qr_path
    }

    return jsonify({
        "status": "pending",
        "transaction_id": transaction_id,
        "item": item,
        "amount": amount,
        "upi_link": upi_link,
        "qr_code": f"/qr/{transaction_id}"
    })

@app.route('/status/<transaction_id>', methods=['GET'])
def status(transaction_id):
    tx = transactions.get(transaction_id)
    if not tx:
        return jsonify({"status": "error", "message": "Transaction not found"}), 404
    return jsonify(tx)

@app.route('/qr/<transaction_id>', methods=['GET'])
def qr_image(transaction_id):
    tx = transactions.get(transaction_id)
    if not tx or not os.path.exists(tx['qr_file']):
        return jsonify({"status": "error", "messsage": "QR code not found"}), 404
    return send_file(tx['qr_file'], mimetype='image/png')

if __name__ == "__main__":
    print(f" Flask running on http://127.0.0.1:{PORT}  (or http://<your-LAN-IP>:{PORT})")
    print("Open /shop in your browser for the UI.")
    app.run(host="0.0.0.0", port=PORT, debug=True)
