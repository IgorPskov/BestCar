// Когда html документ готов (прорисован)
$(document).ready(function () {
    // берем в переменную элемент разметки с id jq-notification для оповещений от ajax
    var successMessage = $("#jq-success-notification");

    // Ловим собыитие клика по кнопке добавить в избранное
    $(document).on("click", ".add-to-favorite", function (e) {
        // Блокируем его базовое действие
        e.preventDefault();

        // Берем элемент счетчика в значке избранного и берем оттуда значение
        var carsInFavoriteCount = $("#cars-in-favorite-count");
        var favoriteCount = parseInt(carsInFavoriteCount.text() || 0);

        // Получаем id продукта 
        var product_id = $(this).data("product-id");
        // Из атрибута href берем ссылку на контроллер django
        var add_to_favorite_url = $(this).attr("href");

        $.ajax({
            type: "POST",
            url: add_to_favorite_url,
            data: {
                product_id: product_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Если товар уже в избранном выводим сообщение об этом
                if (data.already_in_favorite) {
                    successMessage.html(data.warning_message);
                    successMessage.addClass('alert-danger');
                    successMessage.fadeIn(400);
                    setTimeout(function () {
                        successMessage.fadeOut(400);
                    }, 5000);
                } else {
                    // В другом случае также выводим сообщение о добавлении товара в избранное
                    successMessage.html(data.success_message);
                    successMessage.addClass('alert-success');
                    successMessage.fadeIn(400);
                    setTimeout(function () {
                        successMessage.fadeOut(400);
                    }, 5000);
                    
                    // Увеличиваем счетчик товаров в избранном на 1 элемент
                    favoriteCount++;
                    carsInFavoriteCount.text(favoriteCount);
                    
                    // // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
                    var favoriteItemsContainer = $("#favorite-items-container");
                    favoriteItemsContainer.html(data.favorite_items_html);
                }
            },

            error: function (data) {
                console.log("Ошибка при добавлении товара в избранное");
            },
        });
    });




    // Ловим собыитие клика по кнопке удалить товар из корзины
    $(document).on("click", ".remove-from-favorite", function (e) {
        // Блокируем его базовое действие
        e.preventDefault();

        // Берем элемент счетчика в значке корзины и берем оттуда значение
        var carsInFavoriteCount = $("#cars-in-favorite-count");
        var favoriteCount = parseInt(carsInFavoriteCount.text() || 0);

        // Получаем id корзины из атрибута data-cart-id
        var favorite_id = $(this).data("favorite-id");
        // Из атрибута href берем ссылку на контроллер django
        var remove_from_favorite = $(this).attr("href");

        // делаем post запрос через ajax не перезагружая страницу
        $.ajax({

            type: "POST",
            url: remove_from_favorite,
            data: {
                favorite_id: favorite_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Сообщение
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                // Через 7сек убираем сообщение
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 7000);

                // Уменьшаем количество товаров в корзине (отрисовка)
                favoriteCount = data.quantity_deleted - 1;
                carsInFavoriteCount.text(favoriteCount);

                // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
                var favoriteItemsContainer = $("#favorite-items-container");
                favoriteItemsContainer.html(data.favorite_items_html);

            },

            error: function (data) {
                console.log("Ошибка при удалении товара из избранного");
            },
        });
    });




    $(document).on("click", ".add-to-cart", function (e) {
        // Блокируем его базовое действие
        e.preventDefault();

        // Получаем id продукта 
        var product_id = $(this).data("product-id");
        // Из атрибута href берем ссылку на контроллер django
        var add_to_cart_url = $(this).attr("href");

        $.ajax({
            type: "POST",
            url: add_to_cart_url,
            data: {
                product_id: product_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Если товар уже в корзине выводим сообщение об этом
                if (data.already_in_cart) {
                    successMessage.html(data.warning_message);
                    successMessage.addClass('alert-danger');
                    successMessage.fadeIn(400);
                    setTimeout(function () {
                        successMessage.fadeOut(400);
                    }, 5000);
                } else {
                    // В другом случае также выводим сообщение о добавлении товара в корзину
                    successMessage.html(data.success_message);
                    successMessage.addClass('alert-success');
                    successMessage.fadeIn(400);
                    setTimeout(function () {
                        successMessage.fadeOut(400);
                    }, 5000);
                
                    
                    // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
                    var cartItemsContainer = $("#cart-items-container");
                    cartItemsContainer.html(data.cart_items_html);
                }
            },

            error: function (data) {
                console.log("Ошибка при добавлении товара в избранное");
            },
        });
    });


    $(document).on("click", ".remove-from-cart", function (e) {
        // Блокируем его базовое действие
        e.preventDefault();

        // Получаем id корзины из атрибута data-cart-id
        var cart_id = $(this).data("cart-id");
        // Из атрибута href берем ссылку на контроллер django
        var remove_from_cart = $(this).attr("href");

        // делаем post запрос через ajax не перезагружая страницу
        $.ajax({

            type: "POST",
            url: remove_from_cart,
            data: {
                cart_id: cart_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Сообщение
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                // Через 7сек убираем сообщение
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 7000);

                // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

            },

            error: function (data) {
                console.log("Ошибка при удалении товара из корзины");
            },
        });
    });



    // Берем из разметки элемент по id - оповещения от django
    var notification = $('#notification');
    // И через 5 сек. убираем
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 5000);
    }

    $(document).ready(function() {
        setTimeout(function() {
            // Скрыть сообщения
            $(".alert").fadeOut(400, function() {
                // После скрытия очистить контейнер сообщений
                $("#messages-container").empty();
            });
        }, 5000);
    });

    // При клике по значку корзины открываем всплывающее(модальное) окно
    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body');

        $('#exampleModal').modal('show');
    });

    // Событие клик по кнопке закрыть окна корзины
    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    // Обработчик события радиокнопки выбора способа доставки
    $("input[name='requires_delivery']").change(function () {
        var selectedValue = $(this).val();
        // Скрываем или отображаем input ввода адреса доставки
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });

    $("input[name='requires_installment']").change(function () {
        var selectedValue = $(this).val();
        // Скрываем или отображаем input ввода адреса доставки
        if (selectedValue === "1") {
            $(".installment").show();
        } else {
            $(".installment").hide();
        }
    });
});