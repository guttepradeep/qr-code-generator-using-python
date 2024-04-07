{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "599dad55",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import ttk, messagebox\n",
    "import qrcode as qr\n",
    "\n",
    "def generate_qr():\n",
    "    url = url_entry.get()\n",
    "    \n",
    "    if not url:\n",
    "        messagebox.showerror(\"Error\", \"Please enter a URL!\")\n",
    "        return\n",
    "    \n",
    "    try:\n",
    "        img = qr.make(url)\n",
    "        img.save(\"QR_Code.png\")\n",
    "        messagebox.showinfo(\"Success\", \"QR Code generated successfully!\")\n",
    "    except Exception as e:\n",
    "        messagebox.showerror(\"Error\", f\"An error occurred: {e}\")\n",
    "\n",
    "# Create main window\n",
    "root = tk.Tk()\n",
    "root.title(\"QR Code Generator\")\n",
    "\n",
    "# Create and place widgets\n",
    "frame = ttk.Frame(root, padding=\"10\")\n",
    "frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))\n",
    "\n",
    "url_label = ttk.Label(frame, text=\"Enter URL:\")\n",
    "url_label.grid(row=0, column=0, sticky=tk.W, pady=5)\n",
    "\n",
    "url_entry = ttk.Entry(frame, width=40)\n",
    "url_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)\n",
    "\n",
    "generate_button = ttk.Button(frame, text=\"Generate QR Code\", command=generate_qr)\n",
    "generate_button.grid(row=1, columnspan=2, pady=10)\n",
    "\n",
    "# Run the GUI\n",
    "root.mainloop()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
