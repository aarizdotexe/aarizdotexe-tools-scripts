#!/bin/python3
print("Welcome to Crypto-currency GST calculator!")

own = input("Total Amount of Crypto-currency(ETH, BTC, etc) you own(In Rs.): ")
gst = float(0.3)
own_int = float(own)
total_gst = float(own_int * gst)
total = "{:.2f}".format(float(own_int - total_gst))

print(f"Total GST Payable: Rs.{total_gst} only.\nTotal cash in-hand after GST Deduction: Rs.{total} only.\nThankyou!")
