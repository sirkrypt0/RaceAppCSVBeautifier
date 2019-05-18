from tkinter import *
from tkinter import filedialog
from tkinter import ttk


class GUI:
    def __init__(self):
        self.tk = Tk()
        self.tk.geometry("280x320")
        self.tk.resizable(False, False)
        self.tk.title("RaceApp CSV")

        self.title_lbl = Label(self.tk, text="Race App CSV Beautifier", font=("Helvetica", 16))
        self.title_lbl.pack(pady=5)

        # Input items
        self.input_file_lbl = Label(self.tk, text="Input file:", font=("Helvetica", 10))
        self.input_file_lbl.pack()

        self.input_file_path = StringVar()
        self.input_file_path.set("")

        self.input_file_ety = Entry(self.tk, textvariable=self.input_file_path, width=40)
        self.input_file_ety.pack()

        self.input_file_btn = Button(self.tk, text="Open input", command=self.open_input_file_dialog)
        self.input_file_btn.pack(pady=5)

        # Output items
        self.output_file_lbl = Label(self.tk, text="Output file:", font=("Helvetica", 10))
        self.output_file_lbl.pack()

        self.output_file_path = StringVar()
        self.output_file_path.set("")

        self.output_file_ety = Entry(self.tk, textvariable=self.output_file_path, width=40)
        self.output_file_ety.pack()

        self.output_file_btn = Button(self.tk, text="Save output as", command=self.open_output_file_dialog)
        self.output_file_btn.pack(pady=5)

        # Progress bar
        self.progress = ttk.Progressbar(self.tk, orient="horizontal", length=200, mode="determinate")
        self.progress.pack(pady=15)

        # Process input
        self.beautify_btn = Button(self.tk, text="Beautify!", command=self.beautify)
        self.beautify_btn.pack()

        self.tk.mainloop()

    def open_input_file_dialog(self):

        input_path = filedialog.askopenfilename(initialdir="/",
                                                title="Select input csv",
                                                filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
        if len(input_path.strip()) == 0:
            return

        self.input_file_path.set(input_path)
        input_split = input_path.split(".")
        input_split[-2] += "_output"
        output_path = ".".join(input_split)
        self.output_file_path.set(output_path)

        self.input_file_ety.xview(len(input_path))
        self.output_file_ety.xview(len(output_path))

    def open_output_file_dialog(self):
        init_dir = "/".join(self.input_file_path.get().split("/")[:-1])
        output_path = filedialog.asksaveasfilename(initialdir=init_dir,
                                                   title="Select output",
                                                   filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
        if len(output_path.strip()) == 0:
            return

        self.output_file_path.set(output_path)
        self.output_file_ety.xview(len(output_path))

    def beautify(self):
        pass


if __name__ == '__main__':
    g = GUI()
