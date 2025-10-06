from flask import Flask, request, send_from_directory, render_template_string
import numpy as np
import os
from compute_table import compute_t

app = Flask(__name__)

# ---- Placeholder model function -------------------------------------------------
def compute(x: np.ndarray) -> np.ndarray:
    return compute_t(x)

FIELDS = [
    ("eye", "眼别 (1=OD, 2=OS)"),
    ("sex", "性别 (1=男, 2=女)"),
    ("is_adult", "是否成人 (成人=1, <15Y=0)"),
    ("age", "年龄"),
    ("exam_age", "检查年龄"),
    ("al_group", "AL发育分组"),
    ("postop_myopia", "术后是否近视 (正视=0, 近视=-1, 远视=1)"),
    ("amblyopia", "是否弱视 (是=1, 否=0)"),
    ("heart", "Heart (1=正常型, 2=反流型, 3=器质型)"),
    ("gene", "Gene (11=FBN1半胱氨酸取代, 12=FBN1生成半胱氨酸, 13=FBN1其他, 2=ADAMTSL4, 3=ADAMTS17, 4=ASPH, 5=CBS, 6=CPAMD8, 7=SUOX)"),
    ("iol_power", "IOL度数"),
    ("surgery_type", "手术方式 (inbag=1, outofbag=2)"),
    ("pre_logmar", "Pre-LogMar(术前眼部参数)"),
    ("pre_al", "pre-IOLMaster-AL(mm)"),
    ("pre_k1", "pre-IOLMaster-K1(D)"),
    ("pre_k1_axis", "pre-IOLMaster-K1轴位"),
    ("pre_k2", "pre-IOLMaster-K2(D)"),
    ("pre_k2_axis", "pre-IOLMaster-K2轴位"),
    ("pre_acd", "pre-ACD"),
    ("pre_wtw", "pre-WTW"),
    ("z_pre_wtw", "Z-Pre WTW"),
]

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('static/js', filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    values = {}
    result = None

    if request.method == 'POST':
        vector = []
        for key, _ in FIELDS:
            raw = request.form.get(key, '').strip()
            values[key] = raw
            try:
                vector.append(float(raw))
            except ValueError:
                vector.append(0.0)
        x = np.array(vector, dtype=float)
        y = compute(x)
        result = y.tolist()

    with open(os.path.join('static/js', 'template.js'), encoding='utf-8') as f:
        html_template = f.read()

    return render_template_string(html_template, fields=FIELDS, values=values, result=result)

if __name__ == '__main__':
    os.makedirs('static/js', exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
