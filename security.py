import re
import html

def sanitize_input(user_input: str) -> str:
    """تنظيف المدخلات وتأمينها ضد هجمات الحقن"""
    if not isinstance(user_input, str):
        return user_input
    cleaned = html.escape(user_input)
    cleaned = re.sub(r'[;\'"\\--]', '', cleaned)
    return cleaned.strip()
