$(document).ready(function () {
    /* mask for phone */
    $("#id_email").inputmask("*{1,50}[.*{1,50}][.*{1,50}]@*{1,50}.*{1,20}[.*{1,20}][.*{1,20}]");
    $("#id_phone").inputmask("+7 (999) 999-9999");
    $("#id_date_birth").inputmask("99.99.9999");
    
    /* add click basket */
    $(document).on('click', '.add_basket', function (e) {
        e.preventDefault();
        $.ajax({type: 'POST', url: $(this).data("url"),
            data: {
              productid: $(this).data("product"),
              productqty: 1,
              csrfmiddlewaretoken: $(this).data("token"),
              action: 'post'
            },
            success: function (json) {
                updateBasketUI(json)
            },
            error: function (xhr, errmsg, err) {}
        });
        return false;
    });

    /* Delete Item basket */
    $(document).on("click", ".delete_basket", function (e) {
        e.preventDefault();
        var prodid = $(this).data("product");
        $.ajax({type: "POST", url: $(this).data("url"),
        data: {
            productid: prodid,
            csrfmiddlewaretoken: $(this).data("token"),
            action: "post",
        },
        success: function (json) {
            $('.product-item[data-index="' + prodid + '"]').remove();
         
            // update number
            updateBasketUI(json)
        },
        error: function (xhr, errmsg, err) {},
        });

        return false;
    });

    /* update item basket */
    $(document).on("click", ".update_basket", function (e) {
        e.preventDefault();
        var prodid = $(this).data("product");
        $.ajax({type: "POST", url: $(this).data("url"),
          data: {
            productid: prodid,
            productqty: $("#select_id_" + prodid + " option:selected").text(),
            csrfmiddlewaretoken: $(this).data("token"),
            action: "post",
          },
          success: function (json) {
            updateBasketUI(json)
          },
          error: function (xhr, errmsg, err) {},
        });

        return false;
    });

    /* update delivery */
    $(document).on("click", ".update_delivery", function (e) {
        e.preventDefault();
        var delivery_id = $(this).data("delivery");
        var token = $('input[name="csrfmiddlewaretoken"]').val();
        var url = $(this).attr('href');

        $.ajax({type: "POST", url: url,
          data: {
            delivery_id: delivery_id,
            csrfmiddlewaretoken: token,
            action: "post",
          },
          success: function (json) {
            updateBasketUI(json)
          },
          error: function (xhr, errmsg, err) {},
        });
        return false;
    });

    $(document).on("click", ".update_payment", function (e) {
        e.preventDefault();
        var payment_id = $(this).data("payment");
        var token = $('input[name="csrfmiddlewaretoken"]').val();
        var url = $(this).attr('href');

        $.ajax({type: "POST", url: url,
          data: {
            payment_id: payment_id,
            csrfmiddlewaretoken: token,
            action: "post",
          },
          success: function (json) {
            updateBasketUI(json)
          },
          error: function (xhr, errmsg, err) {},
        });
        return false;
    });

    /* images_gallery */
    $(document).on("click", "#images_gallery > div",  function (e) {
        e.preventDefault();
        var img_src = $(this).attr('data-img');
        $('#images_gallery__main').attr('src', img_src);
        $("#images_gallery > div").removeClass("active");
        $(this).addClass('active');
        return false;
    });

    setMapUI('#mapWrap'); /* add map */

    $(document).on('click', 'button.close', function (e) {
        e.preventDefault();
        $('.popup-form').modal('hide');
        return false;
    });

    /* плавный скроулинг якорей */
    $("#navbarSupportedContent").on('click', '[href*="#"]', function(e){
        e.preventDefault();

        if (window.location.pathname != '/') {  window.location.replace($(this).attr('href')); return false; }

        var fixed_offset = 60;
        $('html,body').stop().animate({ scrollTop: $(this.hash).offset().top - fixed_offset }, 800);
        return false;
    });

    /* the submit forms */
    $(document).on("submit", "form.SubmitFormAjax", getFormSubmitAjax);
});

const getFormSubmitAjax = function (event) {
    event.preventDefault();
    var error = false;
    var form_ =  $(this);
    var req = form_.find('[required]'), _submit = form_.find('button[type=submit]');
    req.each(function() {
        /* если не checkbox */
        if($(this).attr('type') != "checkbox") {
            if ($(this).val() == "") {
                $(this).css({'border-color':'#fff'});               
                error = true;
            } else {
                $(this).css({'border-color':'#9a9da0'});
                $(this).parent().find('.req-notice').remove();
            }
        }
        /* если он майл */
        if($(this).attr('type') != "checkbox" && $(this).val() != "" && $(this).attr('type') == 'email') {
            var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
            if(reg.test($(this).val()) == false) {
                $(this).css({'border-color':'#fff'});
                error = true;
            }
        }
        /* если он checkbox */
        if($(this).attr('type') == "checkbox") {
            if($(this).prop("checked") == false){
                $(this).css({'border-color':'#fff'});               
                error = true;
            }else{
                $(this).css({'background':'','border-color':''});
                $(this).parent().parent().find('.req-notice').remove();
            }
        }
    });

    if (error) {
        return false;
    }

    $.ajax({
        url: form_.attr("action"),
        type: form_.attr("method"),
        dataType: "JSON",
        data: new FormData(this),
        processData: false,
        contentType: false,
        beforeSend: function() { },
        complete: function() { },
        success: function (res) {
            dump(res);
            if (res.alert) {
                showMessage(res.alert)
            }
            form_.trigger('reset');
        },
        error: function (res) {            
            if (res.alert) {
                showMessage(res.alert)
            }
            dump(res);
        }
    });

    return false;
}

const clickModal = (title, body) => {
    var popup = document.getElementById('popupModal');

    popup.querySelector('h1').innerHTML = title;
    popup.querySelector('div.modal-body').innerHTML = body;

    var myModal = new bootstrap.Modal(popup);
    myModal.show();
}

const dump = (res) => {
    console.log(JSON.stringify(res,undefined, 2));
}

const isSet = (elmId, value) => {
    let elem = document.getElementById(elmId);
    if (typeof elem !== 'undefined' && elem !== null) {
        elem.innerHTML = value;
    }
}

const rub = (val) => {
    return `${val.toString().replace(",", ".").replace(".00", "")} ₽`;
}

const updateBasketUI = (json) => {
    /* console.log */
    dump(json)
    
    /* update number */
    var arr_key = ["subtotal", "total", "delivery_price"];
    arr_key.forEach(function(item, i) {
        if (item in json) {
            isSet(item, rub(json[item]));
        }
    });

    if ("delivery" in json) {
        isSet('delivery_name', json['delivery']['name']);
        isSet('delivery_price', rub(json['delivery']['price']));
    }

    if ("payment" in json) {
        isSet('payment_name', json['payment']['name']);
    }

    /* print count in basket */
    if ("qty" in json) {
        $('.basket-qty').html(json.qty);
    }
}

const showMessage = function(text, mClass) {
    $(".popup-form").remove();
    $(".modal-backdrop").remove();
    var modalClass = ["modal-md","modal-lg","modal-xl"];
    var mClass = (mClass ? mClass: 0);

    var button_close = $('<button/>', {
        'type': 'button',
        'class': 'close btn',
        'data-dismiss': 'modal',
        'aria-label': 'Close',
    }).append('&times;');

    var modalBody = $('<div/>',{'class':'modal-body'}).append(text);
    /**/
    var modalContent = $('<div/>', {'class':'modal-content'}).append(button_close).append(modalBody);
    var modalDialog = $('<div/>', {
        'class':'modal-dialog modal-dialog-centered ' + modalClass[mClass]
    }).html(modalContent);

    $('<div/>',{
        'class':'popup-form modal fade',
        'data-bs-backdrop':'static',
        'data-bs-keyboard':'false',
        'tabindex':-1,
        'aria-hidde':'true',
    }).append(modalDialog).appendTo('body').modal('show');
}

const setMapUI = (div_id_select) => {
    if ($(div_id_select).length) {
        /* openstreetmap */
        // Define latitude, longitude and zoom level 
        //www.codexworld.com/embed-open-street-map-with-marker-in-html-using-javascript/
        const latitude = 54.720716;
        const longitude = 20.47329;
        const zoom = 17;
        const adress_text = 'проспект Мира, 63';
        
        // Set DIV element to embed map
        var mymap = L.map('mapWrap');
        // Customize the marker icon
        let customIcon = L.icon({
            iconUrl: "/static/img/geo-alt-fill.svg",
            iconSize: [50,50]
        });

        let iconOptions = {
            title: "Адрес координаты",
            draggable: false,
            icon: customIcon
        }
        
        // Add initial marker & popup window
        var mmr = L.marker([0,0], iconOptions);
        mmr.bindPopup('0,0');
        mmr.addTo(mymap);
        
        // Add copyright attribution
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png?{foo}', {
            scrollWheelZoom: false,
            foo: 'bar',
            attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'}
        ).addTo(mymap);
        
        // Set lat lng position and zoom level of map 
        mmr.setLatLng(L.latLng(latitude, longitude));
        mymap.setView([latitude, longitude], zoom);
        mymap.scrollWheelZoom.disable();
        
        // Set popup window content
        mmr.setPopupContent(adress_text).openPopup();
        
        // Set marker onclick event
        mmr.on('click', openPopupWindow);
        
        // Marker click event handler
        function openPopupWindow(e) {
            mmr.setPopupContent(adress_text).openPopup();
        }
    }
}