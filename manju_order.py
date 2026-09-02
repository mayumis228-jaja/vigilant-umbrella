import tkinter as tk
from tkinter import ttk, messagebox

MENU = {
    "いきなりまんじゅう": 250,
    "肉まん": 160,
    "チョコ": 150,
    "いちご": 150,
    "抹茶": 150,
    "ソーダ（白）": 150,
    "やぶれ（黒）": 150,
    "柏餅": 150
}


class ManjuOrderApp:

    def __init__(self, root):
        self.root = root
        self.root.title("注文アプリ")
        self.root.geometry("450x700")
        self.root.resizable(False, False)

        self.spins = {}

        # タイトル
        tk.Label(
            root,
            text="饅頭注文アプリ",
            font=("Meiryo", 20, "bold")
        ).pack(pady=15)

        # ヘッダー
        header = tk.Frame(root)
        header.pack(fill="x", padx=20)

        tk.Label(header, text="商品名",
                 font=("Meiryo", 11, "bold"),
                 width=18, anchor="w").grid(row=0, column=0)

        tk.Label(header, text="単価",
                 font=("Meiryo", 11, "bold"),
                 width=6).grid(row=0, column=1)

        tk.Label(header, text="数量",
                 font=("Meiryo", 11, "bold"),
                 width=6).grid(row=0, column=2)

        ttk.Separator(root).pack(fill="x", padx=20, pady=8)

        # 商品一覧
        item_frame = tk.Frame(root)
        item_frame.pack(padx=20)

        for row, (item, price) in enumerate(MENU.items()):

            tk.Label(
                item_frame,
                text=item,
                width=18,
                anchor="w",
                font=("Meiryo", 11)
            ).grid(row=row, column=0, pady=5, sticky="w")

            tk.Label(
                item_frame,
                text=f"{price}円",
                width=6,
                anchor="e",
                font=("Meiryo", 11)
            ).grid(row=row, column=1, padx=(0, 20))

            spin = tk.Spinbox(
                item_frame,
                from_=0,
                to=99,
                width=5,
                justify="center",
                command=self.update_total,
                font=("Meiryo", 11)
            )

            spin.grid(row=row, column=2)

            spin.bind(
                "<KeyRelease>",
                lambda e: self.update_total()
            )

            self.spins[item] = spin

        ttk.Separator(root).pack(fill="x", padx=20, pady=15)

        self.total_qty_label = tk.Label(
            root,
            text="合計個数：0個",
            font=("Meiryo", 14, "bold")
        )
        self.total_qty_label.pack(pady=5)

        self.total_price_label = tk.Label(
            root,
            text="合計金額：0円",
            font=("Meiryo", 16, "bold"),
            fg="red"
        )
        self.total_price_label.pack(pady=5)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)

        tk.Button(
            btn_frame,
            text="クリア",
            width=12,
            font=("Meiryo", 10),
            command=self.clear_order
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            btn_frame,
            text="注文確定",
            width=12,
            font=("Meiryo", 10),
            command=self.confirm_order
        ).grid(row=0, column=1, padx=10)

    def update_total(self):

        total_qty = 0
        total_price = 0

        for item, spin in self.spins.items():

            try:
                qty = int(spin.get())
            except ValueError:
                qty = 0

            total_qty += qty
            total_price += qty * MENU[item]

        self.total_qty_label.config(
            text=f"合計個数：{total_qty}個"
        )

        self.total_price_label.config(
            text=f"合計金額：{total_price:,}円"
        )

    def clear_order(self):

        for spin in self.spins.values():
            spin.delete(0, tk.END)
            spin.insert(0, "0")

        self.update_total()

    def confirm_order(self):

        lines = []
        total_qty = 0
        total_price = 0

        for item, spin in self.spins.items():

            qty = int(spin.get())

            if qty > 0:
                amount = qty * MENU[item]

                lines.append(
                    f"{item}　{qty}個　{amount:,}円"
                )

                total_qty += qty
                total_price += amount

        if total_qty == 0:
            messagebox.showwarning(
                "確認",
                "数量が入力されていません。"
            )
            return

        messagebox.showinfo(
            "注文内容",
            "\n".join(lines)
            + f"\n\n合計個数：{total_qty}個"
            + f"\n合計金額：{total_price:,}円"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = ManjuOrderApp(root)
    root.mainloop()