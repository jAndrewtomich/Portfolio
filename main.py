from flask import Flask, render_template, url_for


def create_app():
    app = Flask(__name__)
    return app


def main():

    fapp = create_app()

    @fapp.route('/')
    @fapp.route("/index")
    def index():
        return render_template("index.html")

    # @fapp.route("/portfolio-item")
    # def portfolio_item():
    #     return render_template("portfolio-item.html")

    fapp.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
