import re
import html

def sanitize_input(user_input):
    """تنظيف المدخلات وتأمينها ضد هجمات الحقن بشكل آمن تماماً ضد الأخطاء"""
    if isinstance(user_input, str):
        cleaned = html.escape(user_input)
        cleaned = re.sub(r'[;\'"\\--]', '', cleaned)
        return cleaned.strip()
    elif isinstance(user_input, dict):
        # التأكد من أن مفتاح الدكشنري (k) يتحول إلى نص حصراً لكي لا يحدث خطأ unhashable
        return {str(k): sanitize_input(v) for k, v in user_input.items()}
    elif isinstance(user_input, list):
        return [sanitize_input(item) for item in user_input]
    
    return user_input
