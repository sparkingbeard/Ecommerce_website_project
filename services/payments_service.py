import razorpay
from config import RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET
client = razorpay.client(auth = (RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))


client.set_app_details({
    "title": "Ecommerce Website",
    "version": "1.0.0"
})


def create_order(amount):
    return client.order.create({
        "amount" : amount,
        "currency": "INR",
        "receipt": "order_rcptid_11"
    })
