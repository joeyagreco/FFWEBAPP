function initializeTable() {
        $(document).ready( function () {
        $('#owner_comparison_table').DataTable(
            {
                "order": [[ 4, "desc" ]],
                "searching": false,
                "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]]
            }
        );
    } );
}