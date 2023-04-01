<script>

// import Icon from 'svelte-icons-pack/Icon.svelte';
// import FaPlusCircle from 'svelte-icons/fa/FaPlusCircle.svelte'


    let now = new Date();

    
    function generateHours() {
        let hours = [];
        for(let i = 1; i <= 24; i++) {
            hours.push(i+":00");
        }

        return hours


    }

let datum = now.toLocaleDateString('en-UK', {
  day: '2-digit',
  month: 'long',
  year: 'numeric'
});

</script>


<div class="container">

    <div class="logo">
        <h1>Planer UI</h1>
    </div>

    <div class="nav">
        
            <a href="">Home</a>
            <a href="/login">Login</a>
            <a href="">Register</a>
    </div>

</div>

    <div class="date">
        <h3>{datum}</h3>
    </div>

<div class="table">
    <div class="clock">
        <table>
                    {#each generateHours() as hour}
                        <tr>
                            <td>
                                {hour}
                            </td>
                        </tr>
                    {/each}
        </table> 
    </div>

    <div class="timeline">
        <table>
                    {#each generateHours() as hour}
                        <tr>
                            <td>
                                {''}
                            </td>
                            
                            
                        </tr>
                    {/each}
        </table> 
    </div>
    </div>
        

    <!-- <button>
        <Icon src={FaPlusCircle} /> 
    </button> -->

<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap');
    
    *{
        padding: 0;
        margin: 0;
        font-family: 'Roboto', sans-serif;
    }
    .container {
       display: flex;
        width: 100%;
        justify-content: space-evenly;
        align-items: center;
        background-color: #4d6cfa;
        color: whitesmoke;
        padding: 1.1rem;
    }

    .nav {
        display: flex;
        justify-content: flex-end;
        width: 50%;
       
    }

    .nav a{
        margin-right: 3rem;
        text-decoration: none;
        color: whitesmoke;
       
    }

    .date{
        background-color: #e9ebf8;
        display: flex;
        justify-content: center;
        padding: 1rem;
    }

    table{
        background-color: #e9ebf8;
        width:100%;  
       
    }

    .table{
        display: flex;
        width: 100%;
    }

    .clock{
        width:10%;

    }
    
    .timeline{
        width: 90%;
    }

    td{
        padding: 4rem;
        height: 3rem;
        border-bottom:2px solid #bbc5f5 ;
    }
    
</style>