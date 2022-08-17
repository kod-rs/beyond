<template>
    <div id="root">
        <Navigation></Navigation>
        <main class="mt-5 pt-3">
            <div class="container-fluid">

                <div class="row">
                    <div class="col-md-12 mb-3">
                        <div class="card">
                            <div class="card-header">
                                <span><i class="bi bi-table me-2"></i></span> map
                            </div>
                            <div class="card-body">
                                <div class="table-responsive">
                                    <Map />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-md-6 mb-3">
                        <div class="card h-100">
                            <div class="card-header">
                                <span class="me-2"><i class="bi bi-bar-chart-fill"></i></span>
                                Area Chart Example
                            </div>
                            <div class="card-body">
                                <canvas class="chart" width="400" height="200"></canvas>
                                <button>add new location</button>

                                <input type="text" value="name" />
                                <div>x: </div>
                                <div>y:</div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6 mb-3">
                        <div class="card h-100">
                            <div class="card-header">
                                <span class="me-2"><i class="bi bi-bar-chart-fill"></i></span>
                                Area Chart Example
                            </div>
                            <div class="card-body">
                                <canvas class="chart" width="400" height="200"></canvas>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    </div>
</template>

<script>
export default {
}
</script>

<style>
@import './style.css';
#root {
    border-style: solid;
}
</style>
