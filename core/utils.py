
import calendar
from datetime import datetime
from .models import Product

def generate_report(period='monthly'):
    now = datetime.now()
    report = []

    if period == 'monthly':
        month_days = calendar.monthrange(now.year, now.month)[1]
        start_date = datetime(now.year, now.month, 1)
        end_date = datetime(now.year, now.month, month_days)
        title = f"Monthly Report for {now.strftime('%B %Y')}"
    else:  # annual
        start_date = datetime(now.year, 1, 1)
        end_date = datetime(now.year, 12, 31)
        title = f"Annual Report for {now.year}"

    products = Product.objects.filter(date__range=(start_date, end_date))
    total_revenue = sum(p.price * p.quantity for p in products)

    report.append(title)
    report.append(f"Total Revenue: ${total_revenue:.2f}")
    report.append("Product Sales:")
    for product in products:
        report.append(f"{product.name}: {product.quantity} units sold, ${product.price * product.quantity:.2f} revenue")

    return "\n".join(report)
