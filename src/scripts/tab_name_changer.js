
export const activate_tab_name_changer = () => {

    onload = (event) => {
        var title = document.title;

        var titles = [
            "beyond", "BEYOND"
        ];
        var driver = null;

        function getRandomNumber(min, max) {
            return Math.floor(Math.random() * (max - min)) + min;
        }

        document.addEventListener("visibilitychange", function (e) {

            if (document.hidden) {
                driver = setInterval(function () {
                    var prev_title = document.title;
                    var num = getRandomNumber(0, titles.length - 1);
                    document.title = titles[num];

                    if (prev_title === document.title) {
                        if (num === titles.length - 1) {
                            document.title = titles[0]
                        } else {
                            document.title = titles[num + 1];
                        }
                    }

                }, 200);
            } else {
                document.title = title;
                clearInterval(driver);
            }

        });

    };




}