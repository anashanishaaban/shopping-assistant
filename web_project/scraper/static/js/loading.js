<script>
    window.addEventListener('load', (event) => {
        document.getElementById('loading').style.display = 'block'; // Show loading indicator
        fetchProducts(); // You might call this function to start the fetch process if you're using AJAX
    });

    // Function to simulate hiding the loading screen (replace with your actual data loading logic)
    function fetchProducts() {
        // Simulate a network request with setTimeout
        setTimeout(() => {
            document.getElementById('loading').style.display = 'none'; // Hide loading indicator
        }, 20000); // Assuming it takes 20 seconds to load your data; adjust accordingly
    }
</script>
