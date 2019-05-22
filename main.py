from tkinter import *
from tkinter import ttk, messagebox, filedialog
from table import *
from openpyxl import Workbook
import os.path


class GUI:
    def __init__(self):
        self.work_stopped = False
        self.init_dir = "/"

        self.tk = Tk()
        self.tk.geometry("280x370")
        self.tk.resizable(False, False)
        self.tk.title("RaceApp CSV to Excel")

        self.title_lbl = Label(self.tk, text="Race App CSV to Excel", font=("Helvetica", 16))
        self.title_lbl.pack(pady=5)

        # Input items
        self.input_file_lbl = Label(self.tk, text="Input file:", font=("Helvetica", 10))
        self.input_file_lbl.pack()

        self.input_file_path = StringVar()
        self.input_file_path.set("")

        self.input_file_ety = Entry(self.tk, textvariable=self.input_file_path, width=30)
        self.input_file_ety.pack()

        self.input_file_btn = Button(self.tk, text="Select input file ...", command=self.open_input_file_dialog)
        self.input_file_btn.pack(pady=5)

        # Output items
        self.output_file_lbl = Label(self.tk, text="Output file:", font=("Helvetica", 10))
        self.output_file_lbl.pack()

        self.output_file_path = StringVar()
        self.output_file_path.set("")

        self.output_file_ety = Entry(self.tk, textvariable=self.output_file_path, width=30)
        self.output_file_ety.pack()

        self.output_file_btn = Button(self.tk, text="Select output file ...", command=self.open_output_file_dialog)
        self.output_file_btn.pack(pady=5)

        # Progressbar reading
        self.prog_read_lbl = Label(self.tk, text="READING", font=("Helvetica", 10))
        self.prog_read_lbl.pack(pady=5)

        self.progress_reading = ttk.Progressbar(self.tk, orient="horizontal", length=200, mode="determinate")
        self.progress_reading.pack()

        # Progressbar writing
        self.prog_write_lbl = Label(self.tk, text="WRITING", font=("Helvetica", 10))
        self.prog_write_lbl.pack(pady=5)

        self.progress_writing = ttk.Progressbar(self.tk, orient="horizontal", length=200, mode="determinate")
        self.progress_writing.pack()

        # Process input
        self.beautify_btn = Button(self.tk, text="To Excel!", command=self.beautify)
        self.beautify_btn.pack(pady=5)

        self.tk.mainloop()

    def open_input_file_dialog(self):

        input_path = filedialog.askopenfilename(initialdir="/",
                                                title="Select input csv",
                                                filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
        if len(input_path.strip()) == 0:
            return

        self.input_file_path.set(input_path)
        input_split = input_path.split(".")
        input_split[-1] = "xlsx"
        output_path = ".".join(input_split)
        self.output_file_path.set(output_path)

        self.input_file_ety.xview(len(input_path))
        self.output_file_ety.xview(len(output_path))

    def open_output_file_dialog(self):
        init_dir = self.init_dir.join(self.input_file_path.get().split("/")[:-1])
        output_path = filedialog.asksaveasfilename(initialdir=init_dir,
                                                   title="Select output",
                                                   filetypes=(("XLSX files", "*.xlsx"), ("all files", "*.*")))
        if len(output_path.strip()) == 0:
            return

        self.output_file_path.set(output_path)
        self.output_file_ety.xview(len(output_path))

    def reset_progress(self):
        self.progress_reading["value"] = 0
        self.progress_reading["maximum"] = 1
        self.progress_writing["value"] = 0
        self.progress_writing["maximum"] = 1

    def change_gui_state(self, active=True):
        _state = "normal" if active else "disabled"

        self.input_file_ety.config(state=_state)
        self.input_file_btn.config(state=_state)
        self.output_file_ety.config(state=_state)
        self.output_file_btn.config(state=_state)

        if active:
            self.beautify_btn.config(text="To excel!", command=self.beautify)
        else:
            self.beautify_btn.config(text="Cancel", command=lambda: self.leave_work_mode(True))

    def enter_work_mode(self):
        self.change_gui_state(False)
        self.reset_progress()

        self.work_stopped = False

    def leave_work_mode(self, cancel=False):
        if cancel:
            result = messagebox.askquestion("Cancel",
                                            "Are you sure that you want to cancel?",
                                            icon="warning")
            if result != "yes":
                return

            self.reset_progress()
        self.change_gui_state(True)

        self.work_stopped = True

    def beautify(self):
        if os.path.isfile(self.output_file_path.get()):
            result = messagebox.askquestion("Overwriting",
                                            "Output file already exists! Do you want to overwrite it?",
                                            icon="warning")
            if result != "yes":
                return

        self.enter_work_mode()

        try:
            input_file = open(self.input_file_path.get(), "r")
            input_data = input_file.readlines()
            input_file.close()
        except FileNotFoundError as e:
            messagebox.showerror("Open error", "Error opening file: "+e.strerror)
            self.leave_work_mode(True)
            return
        except PermissionError as e:
            messagebox.showerror("Open error", "Error opening file: " + e.strerror + "Maybe it's still opened?")
            self.leave_work_mode(True)
            return

        try:
            if os.path.isfile(self.output_file_path.get()):
                output_file = open(self.output_file_path.get(), "r")
                output_file.close()
        except PermissionError as e:
            messagebox.showerror("Open error", "Error opening file: " + e.strerror + "Maybe it's still opened?")
            self.leave_work_mode(True)
            return

        # Start time is always defined in the second last line
        start_time = int(input_data[-2].split(",")[-1])

        # Stop time is always defined in the last line
        stop_time_full = int(input_data[-1].split(",")[-1])
        stop_time = stop_time_full - start_time

        # Init table with all rows, add 1 as we want stop_time to be part of table
        # Might be very slow
        # table = {i: TableEntry() for i in range(stop_time+1)}
        table = {}

        current_reading_operation_amount = 0
        self.progress_reading["maximum"] = len(input_data)

        for line in input_data[1:-2]:
            self.tk.update()
            self.tk.update_idletasks()

            self.progress_reading["value"] = current_reading_operation_amount
            line_array = line.split(",")
            timestamp_large = int(line_array[-1])
            timestamp = float(timestamp_large-start_time)/1000.0

            # If we find a value that was recorded before lap started or after stopped ignore it
            if timestamp < 0 or timestamp > stop_time:
                continue

            if timestamp not in table:
                table[timestamp] = TableEntry(start_time, timestamp_large, timestamp)

            table[timestamp].add_from_line_array(line_array)

            current_reading_operation_amount += 1

            if self.work_stopped:
                self.progress_reading["value"] = 0
                return

        writing_operation_amount = len(table)
        current_writing_operation_amount = 0
        self.progress_writing["maximum"] = writing_operation_amount

        cols = [d.value for d in DataType]
        # Create new Excel workbook and sheet
        book = Workbook()
        sheet = book.active
        current_index = 0

        # Ignore the GEOLOCATION as we split it up into 4 values
        sheet.append(cols[1:])
        for time_row in sorted(table.items()):
            self.tk.update()
            self.tk.update_idletasks()
            self.progress_writing["value"] = current_writing_operation_amount

            sheet.append(time_row[1].get_entry())
            current_index += 1

            current_writing_operation_amount += 1

            if self.work_stopped:
                del book
                self.progress_writing["value"] = 0
                return

        book.save(self.output_file_ety.get())

        self.leave_work_mode()
        messagebox.showinfo("CSV to Excel done!", "The CSV has been successfully converted to XLSX!")


if __name__ == '__main__':
    g = GUI()
