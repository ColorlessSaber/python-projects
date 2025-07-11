"""
Python Ver: 3.13

Author: Michael Heilman

Purpose: An application that automatically creates a basic HTML web page that says
"Stay tuned for our amazing summer sale!" This application is created using Tkinter GUI and Python.
"""
import tkinter as tk
import webbrowser

class ParentWindow(tk.Frame):
    def __init__(self, primary):
        super().__init__()

        # creation of the window
        self.primary = primary
        self.primary.title("Web page Generator")

        # entry to accept custom text
        self.label_custom_text = tk.Label(self.primary, text="Enter custom text or click the Default HTML page button")
        self.label_custom_text.grid(row=0, column=0, padx=(10,0))
        self.entry_custom_text = tk.Entry(self.primary, width=120)
        self.entry_custom_text.grid(row=1, column=0, columnspan=3, padx=(10,0), pady=(0,0))

        # button for generating default HTML page
        self.btn_default_html_page = tk.Button(self.primary, text='Default HTML Page', width=30, height=2, command=lambda: self.generate_html_page("default"))
        self.btn_default_html_page.grid(row=2, column=1, padx=(0,10), pady=(10,10))

        # button for generating HTML page using custom text
        self.btn_custom_text_html_page = tk.Button(self.primary, text='Submit Custom Text', width=30, height=2, command=lambda: self.generate_html_page("custom"))
        self.btn_custom_text_html_page.grid(row=2, column=2, padx=(10,10), pady=(10,10))

    def generate_html_page(self, button_pushed):
        """
        Depending on the button that was pushed, either creates a default HTML webpage or an HTML webpage with custom
        text.
        Default - creates a default HTML webpage
        Custom - creates an HTML webpage with user inputted text.
        """
        if button_pushed is 'default':
            html_text = "Stay tuned for our amazing summer sale!"
        else:
            html_text = self.entry_custom_text.get()
        html_file = open("index.html", "w")
        html_content = "<html>\n<body>\n<h1>{}</h1>\n</body>\n</html>".format(html_text)
        html_file.write(html_content)
        html_file.close()
        webbrowser.open_new_tab("index.html")

if __name__ == '__main__':
    root = tk.Tk()
    app = ParentWindow(root)
    root.mainloop()