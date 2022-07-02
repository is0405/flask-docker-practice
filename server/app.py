from flask import Flask, render_template, url_for, request

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

# index にアクセスされた場合の処理
@app.route('/', methods=['GET'])
def index():
    message = ""

    # GETメソッドの場合
    if request.method == 'GET':
        # リクエストフォームから「名前」を取得
        id_num = request.args.get('id')
        rad_num = request.args.get('rad')
        
        return render_template('index.html',
                               ID=id_num, rad=rad_num, message="クエリにidとradを指定してください")


if __name__ == "__main__":
    app.debug = True  # デバッグモード有効化
    # app.run(host="0.0.0.0", port=5000)
    app.run()
