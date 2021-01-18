let ar = ['pregnancies', 'glucose', 'blood_pressure', 'skin_thickness', 'insulin', 'bmi', 'age'];
for (var i = 0; i < ar.length; i++) {
    const updateTextInputValue = ar[i] + 'Value';
    document.getElementById(ar[i]).oninput = function() {
        document.getElementById(updateTextInputValue).innerHTML = this.value;
    }
}

const myForm = document.getElementById('myForm');
myForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/predict', {
        method: 'post',
        body: formData
    }).then(function(response) {
        return response.text();
    }).then(function(text) {
        document.getElementById('prediction-text-id').innerHTML = text;
        if (text.startsWith('Woah!')) {
            try {
                document.getElementById('prediction-text-id').classList.remove('prediction-text-bad');
            } catch (e) {
                console.log(e);
            }
            document.getElementById('prediction-text-id').classList.add('prediction-text-good')
        } else {
            try {
                document.getElementById('prediction-text-id').classList.remove('prediction-text-good');
            } catch (e) {
                console.log(e);
            }
            document.getElementById('prediction-text-id').classList.add('prediction-text-bad')
        }
    }).catch(function(err) {
        console.error(err);
    });
});