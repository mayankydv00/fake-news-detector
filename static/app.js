const button = document.getElementById('button')

button.addEventListener('click', async (event) => {
    event.preventDefault();
    //console.log('here');
    const authorName = document.getElementById('author').value;
    const title = document.getElementById('title').value;
    const text = document.getElementById('text').value;
    const responseArea = document.getElementById('responseArea');
    responseArea.innerHTML = '';
    if(authorName && title && text){

        const res = await fetch('/',{
            method: 'POST',
            headers: {
                'Content-type' : 'application/json' 
            },
            body : JSON.stringify({
                authorName,
                title,
                text
            })
        });

        const data = await res.json();
        console.log(data)
        if(data === true){
            responseArea.innerHTML = 'The news is real.';
        }else{
            responseArea.innerHTML = 'The news is fake.';
        }

    }else{
        
        responseArea.innerHTML = 'Please Enter All Values';
    }
    
})