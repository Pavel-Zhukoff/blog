if (document.getElementsByTagName('label')) {
    let labels = document.getElementsByTagName('label');
    for (let i = 0; i < labels.length; i++) {

        if (document.getElementById(labels[i].getAttribute('for')).required) {
            labels[i].className += ' label-required';
        }
    }
} 