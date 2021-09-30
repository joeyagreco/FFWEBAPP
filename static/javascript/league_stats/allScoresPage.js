function initializeTable() {
    $(document).ready( function () {
        $('#all_scores_table').DataTable(
            {
                "order": [[ 0, "desc" ]],
                "searching": false,
                "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]]
            }
        );
    } );
}