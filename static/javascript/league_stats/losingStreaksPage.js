function initializeTable() {
    $(document).ready( function () {
        $('#streaks_table').DataTable(
            {
                "order": [[ 0, "desc" ]],
                "searching": false,
                "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]]
            }
        );
    } );
}