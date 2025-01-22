from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def generate_utility_bill_pdf(path, bill_info):
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4
    c.setTitle("Utility Bill")

    # Header Section
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(colors.darkblue)
    c.drawString(200, height - 80, "Utility Bill")

    # Utility Provider Information
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    c.drawString(50, height - 120, "Issued by: Unified City Service Provider")

    # User Information
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 160, "User Information")
    c.setFont("Helvetica", 12)
    c.drawString(70, height - 180, f"User CNIC: {bill_info['user_cnic']}")
    c.drawString(70, height - 200, f"Bill Type: {bill_info['bill_type']}")
    c.drawString(70, height - 220, f"Issue Date: {bill_info['issue_date']}")
    c.drawString(70, height - 240, f"Due Date: {bill_info['due_date']}")

    # Bill Details Table Header
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.gray)
    c.rect(50, height - 270, 500, 20, fill=True)
    c.setFillColor(colors.white)
    c.drawString(60, height - 265, "Description")
    c.drawString(230, height - 265, "Amount (Rs.)")

    # Bill Details
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    y_position = height - 290

    # Amount before due
    c.drawString(60, y_position, "Amount Before Due")
    c.drawString(240, y_position, f"{bill_info['amount_before_due']:.2f}")
    y_position -= 20

    # Tax Details
    c.drawString(60, y_position, f"Tax ({bill_info['tax_percentage']}%)")
    c.drawString(240, y_position, f"{bill_info['tax_amount']:.2f}")
    y_position -= 20

    # Late Fee
    c.drawString(60, y_position, "Late Fee (10%)")
    c.drawString(240, y_position, f"{bill_info['late_fee']:.2f}")
    y_position -= 20

    # Total Amount
    c.setFont("Helvetica-Bold", 12)
    c.drawString(240, y_position, "Total Amount Due")
    c.drawString(420, y_position, f"{bill_info['amount_after_due']:.2f}")
    y_position -= 40

    # Footer
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.black)
    c.drawString(50, y_position, "Thank you for using our service. Please pay your bill before the due date.")

    # Save the PDF
    c.save()
    print(f"Utility bill saved to: {path}")


if __name__ == "__main__":
    bill_info_example = {
        "user_cnic": "12345-6789012-3",
        "bill_type": "Electricity",
        "issue_date": "2025-01-01",
        "due_date": "2025-01-15",
        "amount_before_due": 5000.00,
        "tax_percentage": 10, 
        "tax_amount": 500.00, 
        "late_fee": 550.00,   
        "amount_after_due": 6050.00  
    }


    generate_utility_bill_pdf("utility_bill_updated.pdf", bill_info_example)
