<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>眼科参数预测 Demo</title>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <style>
    body { font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, PingFang SC, Noto Sans SC, Helvetica, Arial, "Apple Color Emoji", "Segoe UI Emoji"; margin: 0; background:#f6f7fb; }
    .container { max-width: 1100px; margin: 32px auto; padding: 0 16px; }
    .card { background: #fff; border-radius: 16px; box-shadow: 0 6px 24px rgba(0,0,0,0.08); padding: 24px; }
    h1 { font-size: 22px; margin: 0 0 16px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 16px; }
    .field { display:flex; flex-direction:column; }
    label { font-size: 13px; color: #374151; margin-bottom: 6px; }
    input[type=number] { border: 1px solid #e5e7eb; border-radius: 10px; padding: 10px 12px; font-size: 14px; outline: none; }
    input[type=number]:focus { border-color: #6366f1; box-shadow: 0 0 0 3px rgba(99,102,241,0.15); }
    .hint { color:#6b7280; font-size: 12px; margin-top: 6px; }
    .actions { margin-top: 16px; display:flex; gap:12px; }
    button { background:#4f46e5; color:#fff; border:none; border-radius: 12px; padding: 10px 16px; font-size:14px; cursor:pointer; }
    button.secondary { background: #0ea5e9; }
    table { width:100%; border-collapse: collapse; overflow: hidden; border-radius: 12px; }
    th, td { text-align: left; padding: 10px 12px; border-bottom: 1px solid #f1f5f9; }
    thead th { background:#f8fafc; font-weight: 600; }
    .empty { color:#64748b; font-size:14px; padding: 8px 2px; }
    .footer { color:#94a3b8; font-size:12px; margin-top:12px; }
  </style>
</head>
<body>
  <div class="container">
    <div class="card">
      <h1>眼科参数预测 Demo</h1>
      <form method="post" action="/">
        <div class="grid">
          {% for field_name, label in fields %}
          <div class="field">
            <label for="{{ field_name }}">{{ label }}</label>
            <input type="number" step="any" name="{{ field_name }}" id="{{ field_name }}" value="{{ values.get(field_name, '') }}" placeholder="请输入数值" required />
          </div>
          {% endfor %}
        </div>
        <div class="actions">
          <button type="submit">提交并计算</button>
          <button type="button" class="secondary" onclick="document.querySelector('form').reset()">清空</button>
        </div>
      </form>
    </div>

    <div class="card" style="margin-top:16px">
      <h1>计算结果</h1>
      {% if result is not none %}
        {% if result and result|length > 0 %}
        <table>
          <thead>
            <tr>
              <th>IOL度数</th>
              <th>1m-矫正球镜度数 (D)</th>
            </tr>
          </thead>
          <tbody>
            {% for row in result %}
            <tr>
              <td>{{ row[0] }}</td>
              <td>{{ row[1] }}</td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
        {% else %}
          <div class="empty">暂无数据。</div>
        {% endif %}
      {% else %}
        <div class="empty">提交表单后在此显示结果。</div>
      {% endif %}
      <div class="footer">提示</div>
    </div>
  </div>
</body>
</html>
