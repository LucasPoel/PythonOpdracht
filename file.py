import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Giraffe Login")

# Create the login frame
login_frame = tk.Frame(window)

# Create the username and password labels and entry widgets
username_label = tk.Label(login_frame, text="Username:")
username_entry = tk.Entry(login_frame)
password_label = tk.Label(login_frame, text="Password:")
password_entry = tk.Entry(login_frame, show="*")

# Place the widgets in the login frame
username_label.grid(row=0, column=0, sticky="E")
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0, sticky="E")
password_entry.grid(row=1, column=1)

# Create the function to check the login credentials
def check_login():
    # Get the username and password entered by the user
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password are correct
    if username == "giraffe" and password == "giraffe":
        # If the login is successful, display the giraffe picture
        show_picture()
    else:
        # If the login is unsuccessful, display an error message
        tk.messagebox.showerror("Error", "Incorrect username or password")

# Create the login button
login_button = tk.Button(login_frame, text="Login", command=check_login)
login_button.grid(row=2, column=1, sticky="W")

# Place the login frame in the main window
login_frame.pack()

# Create the function to display the giraffe picture
def show_picture():
    # Create a label to hold the giraffe image
    image_label = tk.Label(window)

    # Load the giraffe image
    image = tk.PhotoImage(file="Knipsel.PNG")

    # Set the image label's image
    image_label.config(image=image)
    image_label.image = image

    # Place the image label in the main window
    image_label.pack()

    

# Run the Tkinter event loop
window.mainloop()