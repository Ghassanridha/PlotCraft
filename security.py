import re
import html

def sanitize_input(user_input):
    """تنظيف المدخلات وتأمينها ضد هجمات الحقن بشكل يدعم النصوص والـ Dict"""
    if isinstance(user_input, str):
        cleaned = html.escape(user_input)
        cleaned = re.sub(r'[;\'"\\--]', '', cleaned)
        return cleaned.strip()
    elif isinstance(user_input, dict):
        # تنظيف محتويات الدكشنري بشكل آمن بدل إرجاعه كـ dict عاري قد يسبب خطأ
        return {k: sanitize_input(v) for k, v in user_input.items()}
    elif isinstance(user_input, list):
        return [sanitize_input(item) for item in user_input]
    
    return user_input
