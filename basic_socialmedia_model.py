import mysql.connector
import tkinter as tk
from tkinter import messagebox, simpledialog

mydb = mysql.connector.connect(
    host ="localhost",
    user= "Harsh Vashishtha",
    password = "Harsh@1234",
    database = "SocialMedia"
    )

mycursor = mydb.cursor()

'''mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
'''



#mycursor.execute("CREATE TABLE login ( id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50) UNIQUE, password VARCHAR(50))")
#mycursor.execute('''
    #CREATE TABLE IF NOT EXISTS post (
    #id INT AUTO_INCREMENT PRIMARY KEY,
    #user_id INT,
    #content TEXT,
    #created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    #)
#''')


root = tk.Tk()
root.title("Social Lite")
root.geometry("800x800")
root.resizable(False,False)

current_user= None

def signup():
    username = simpledialog.askstring("Signup", "Enter username : ")
    password = simpledialog.askstring("Signup","Enter password : ")
    if username and password:
        try:
            mycursor.execute("INSERT INTO login ( username,password) VALUES (%s,%s)",(username,password))
            mydb.commit()
            messagebox.showinfo("Success", "Signup Successfully ! please login into your account")
        except:
            messagebox.showinfo("Error","Username is already exists")

def login():
    global current_user
    username = simpledialog.askstring("Signin","Enter username : ")
    password = simpledialog.askstring("Signin","Enter password : ",show ="*")

    mycursor.execute("SELECT * FROM login WHERE username =%s and password = %s",(username,password))
    user = mycursor.fetchone()

    if user:
        current_user = user
        messagebox.showinfo("Success","You have logged in into your account successfully")
        show_feed()

    else:
        messagebox.showerror("Error","Invalid Credentials..")

def create_post():
    if not current_user:
        messagebox.showwarning("Login Required","Please Login first!")
        return


    content = simpledialog.askstring("New Post", "What's on your mind?")
    if content:
        mycursor.execute("INSERT INTO post(user_id,content)VALUES(%s,%s)", (current_user[0],content))
        mydb.commit()
        messagebox.showinfo("Success","Post Created Successfully")
        show_feed()
def show_feed():
    feed_frame.delete(1.0,tk.END)
    mycursor.execute("""
        SELECT login.username, post.content, post.created_at
        FROM post
        JOIN login ON post.user_id = login.id
        ORDER BY post.created_at DESC
    """)
    post = mycursor.fetchall()

    for posts in post:
        feed_frame.insert(tk.END, f"{posts[0]}: {posts[1]}\n({posts[2]})\n\n")
        


btn_signup  = tk.Button(root, text = "signup", command = signup, width = 10, bg = "lightblue")
btn_signup.pack(pady=5)

btn_login = tk.Button(root,text = "login", command = login, width = 10, bg ="lightgreen")
btn_login.pack(pady=5)

btn_post = tk.Button(root, text = "New Post", command = create_post, width = 10,bg ="lightyellow")
btn_post.pack(pady=5)

feed_frame = tk.Text(root, height = 25, width = 70, wrap = "word")
feed_frame.pack(pady=10)
root.mainloop()
        

