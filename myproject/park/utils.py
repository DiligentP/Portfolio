import os
import markdown2
from config import settings
from django.utils.safestring import mark_safe

# pip install markdown
# def mark(markdown_text):
#     extensions = ["nl2br", "fenced_code"]
#     return mark_safe(markdown.markdown(markdown_text, extensions=extensions))


# pip install markdown2
def mark(markdown_filepath):

    # 마크다운 파일을 가져옵니다.
    md_file_path = os.path.join(settings.STATICFILES_DIRS[1], markdown_filepath)

    # md 파일을 읽어 HTML 파일로 변환합니다.
    with open(md_file_path, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    html = mark_safe(markdown2.markdown(markdown_text))

    return html
