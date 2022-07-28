<!-- <template>
    <div>
        <p>page 2</p>
    </div>

    <nav class="navbar navbar-light bg-light">
        <form class="form-inline">
            <input class="form-control mr-sm-2" type="search" placeholder="type location" aria-label="Search">
        </form>
    </nav>

    <div class="row">
        <div class="col p-3 bg-primary text-white">search


        </div>
        <div class="col p-3 bg-dark text-white">map placeholder</div>
        <div class="col p-3 bg-primary text-white">select options</div>
    </div>



</template>
 -->





<template>
    <div id="wrap">
        <div id="tf">
            <div class="cell cell-map">
                Map
            </div>
            <div class="cell cell-edit">
                Edit
            </div>
            <div class="cell cell-inspect">
                Inspect
            </div>
        </div>

    </div>
</template>

<style>
#wrap {
    height: 100%;
    margin: 0;
    border: 2px solid black;

}



#tf {


    font-family: Avenir, Helvetica, Arial, sans-serif;
    height: 100%;
    display: grid;
    grid-template-columns: 100vh;
    grid-auto-rows: 1fr;
    grid-gap: 1rem;
    padding: 1rem;
    box-sizing: border-box;
}

.cell {
    border: 1mm solid black;
    border-radius: 4px;
    background-color: lightgrey;
}

.cell-map {
    grid-column: 1;
    grid-row-start: 1;
    grid-row-end: 3;
}

.cell-edit {
    grid-column: 2;
    grid-row: 1;
}

.cell-inspect {
    grid-column: 2;
    grid-row: 2;
}
</style>