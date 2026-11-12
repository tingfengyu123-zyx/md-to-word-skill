import os, subprocess, sys, zipfile

PANDOC = os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Programs', 'pandoc', 'pandoc.exe')

def main():
    if len(sys.argv) < 2:
        print('用法: python convert.py <输入.md> [输出.docx]')
        return
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(src)[0] + '.docx'

    if not os.path.exists(PANDOC):
        print('没找到 pandoc:', PANDOC)
        return
    subprocess.run([PANDOC, src, '-o', dst, '--from', 'markdown', '--to', 'docx'], check=True)

    _set_songti(dst)
    with zipfile.ZipFile(dst) as z:
        xml = z.read('word/document.xml').decode('utf-8')
    print('输出:', dst)
    print('公式数', xml.count('<m:oMath'), '段落', xml.count('</w:p>'))

def _set_songti(p):
    from docx import Document
    from docx.shared import Pt, Cm
    from docx.oxml.ns import qn
    d = Document(p)
    st = d.styles['Normal']
    st.font.name = '宋体'
    st.font.size = Pt(11)
    st.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    for s in d.sections:
        s.top_margin = Cm(2.0); s.bottom_margin = Cm(2.0)
        s.left_margin = Cm(2.2); s.right_margin = Cm(2.2)
    d.save(p)

if __name__ == '__main__':
    main()
