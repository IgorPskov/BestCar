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
                    
                    // // Меняем содержимое избранного на ответ от django (новый отрисованный фрагмент разметки избранного)
                    var favoriteItemsContainer = $("#favorite-items-container");
                    favoriteItemsContainer.html(data.favorite_items_html);
                }
            },

            error: function (data) {
                console.log("Ошибка при добавлении товара в избранное");
            },
        });
    });




    // Ловим собыитие клика по кнопке удалить товар из избранного
    $(document).on("click", ".remove-from-favorite", function (e) {
        // Блокируем его базовое действие
        e.preventDefault();

        // Берем элемент счетчика в значке избранного и берем оттуда значение
        var carsInFavoriteCount = $("#cars-in-favorite-count");
        var favoriteCount = parseInt(carsInFavoriteCount.text() || 0);

        // Получаем id корзины из атрибута data-favorite-id
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

                // Уменьшаем количество товаров в избранном (отрисовка)
                favoriteCount = data.quantity_deleted - 1;
                carsInFavoriteCount.text(favoriteCount);

                // Меняем содержимое избранного на ответ от django (новый отрисованный фрагмент разметки избранного)
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


    // Интерактивная карта для доставки
    let center = [59.822693, 30.324582];

    function init() {
        // Стоимость за километр.
        var DELIVERY_TARIFF = 20,
        // Минимальная стоимость.
            MINIMUM_COST = 500,
            myMap = new ymaps.Map('map', {
                center: center,
                zoom: 7,
                controls: []
            }),

            // Создадим панель маршрутизации.
            routePanelControl = new ymaps.control.RoutePanel({
                options: {
                    // Добавим заголовок панели.
                    showHeader: true,
                    title: 'Расчёт доставки',
                    autofocus: false,
                },
            }),
            zoomControl = new ymaps.control.ZoomControl({
                options: {
                    size: 'small',
                    float: 'none',
                    position: {
                        bottom: 145,
                        right: 10
                    }
                }
            });
    
        let placemark = new ymaps.Placemark(center, {
            balloonContentHeader: 'Автосалон BestCar',
            balloonContentBody: 'Автомобили находятся здесь',
            balloonContentFooter: 'Расчет расстояния и стоимости доставки происходит отсюда',
        });

        // Пользователь сможет построить только автомобильный маршрут.
        routePanelControl.routePanel.options.set({
            types: {auto: true},
            allowSwitch: false,
            autofocus: false,
        });
    

        routePanelControl.routePanel.state.set({
            fromEnabled: false,
            from: center,
         });
    
        myMap.controls.add(routePanelControl).add(zoomControl);
    
        // Получим ссылку на маршрут.
        routePanelControl.routePanel.getRouteAsync().then(function (route) {
    
            // Зададим максимально допустимое число маршрутов, возвращаемых мультимаршрутизатором.
            route.model.setParams({results: 1}, true);
    
            // Повесим обработчик на событие построения маршрута.
            route.model.events.add('requestsuccess', function () {
                var to = routePanelControl.routePanel.state.get('to');
                if (to) {
                    // Проверяем, находится ли точка в пределах России
                    isInRussia(to, function(inRussia) {
                        if (!inRussia) {
                            alert('Пожалуйста, выберите точку в России.');
                            routePanelControl.routePanel.state.set('to', null);
                        } else {

                        getAddress(to, function(address) {
                            $("#id_delivery_address").val(address); // Выводим в textarea полный адрес
                        });

                            var activeRoute = route.getActiveRoute();
                            if (activeRoute) {
                                // Получим протяженность маршрута.
                                var length = route.getActiveRoute().properties.get("distance"),
                                // Вычислим стоимость доставки.
                                    price = calculate(Math.round(length.value / 1000)),
                                // Создадим макет содержимого балуна маршрута.
                                    balloonContentLayout = ymaps.templateLayoutFactory.createClass(
                                        '<span>Расстояние: ' + length.text + '.</span><br/>' +
                                        '<span style="font-weight: bold; font-style: italic">Стоимость доставки: ' + price + ' р.</span>');
                                // Зададим этот макет для содержимого балуна.
                                route.options.set('routeBalloonContentLayout', balloonContentLayout);
                                // Откроем балун.
                                activeRoute.balloon.open();
                                //Выводим в input цену
                                var priceWithRub = price + " руб.";
                                $("#id_delivery_price").val(priceWithRub);
                            }
                        }
                    });
                };           
            });

        myMap.geoObjects.add(placemark);
    
        });
        // Функция, вычисляющая стоимость доставки.
        function calculate(routeLength) {
            return Math.max(routeLength * DELIVERY_TARIFF, MINIMUM_COST);
        }

         // Функция, проверяющая, находится ли точка в России.
        function isInRussia(point, callback) {
            var geocoder = ymaps.geocode(point);
            geocoder.then(
                function (res) {
                    var firstGeoObject = res.geoObjects.get(0);
                    if (firstGeoObject) {
                        var countryCode = firstGeoObject.properties.get('metaDataProperty.GeocoderMetaData.Address.country_code');
                        callback(countryCode === 'RU');
                    }
                }
            );
        }

        // Функция, получающая полный адрес точки.
        function getAddress(point, callback) {
            var geocoder = ymaps.geocode(point);
            geocoder.then(
                function (res) {
                    var firstGeoObject = res.geoObjects.get(0);
                    if (firstGeoObject) {
                        var address = firstGeoObject.getAddressLine();
                        callback(address);
                    }
                }
            );
        }

        function showRoutePanel() {
            // Показываем панель маршрутизации
            routePanelControl.options.set('visible', true);
            // Показываем панель масштабирования
            zoomControl.options.set('visible', true);
        }
        
        function hideRoutePanel() {
            // Скрываем панель маршрутизации
            routePanelControl.options.set('visible', false);
            // Скрываем панель масштабирования
            zoomControl.options.set('visible', false);
        }

        // Обработчик события радиокнопки выбора способа доставки
        $("input[name='requires_delivery']").change(function () {
            var selectedValue = $(this).val();
            // Скрываем или отображаем input ввода адреса доставки
            if (selectedValue === "1") {
                showRoutePanel();
            } else {
                hideRoutePanel();
            }
    });

    }

    ymaps.ready(init);



    // Берем из разметки элемент по id - оповещения от django
    var notification = $('#notification');
    // И через 5 сек. убираем
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 5000);
    };

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
            $("#deliveryPriceField").show();
        } else {
            $("#deliveryAddressField").hide();
            $("#deliveryPriceField").hide();
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



