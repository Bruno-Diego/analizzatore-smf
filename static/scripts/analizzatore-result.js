// Select the .tabs element
var el = document.getElementsByClassName('tabs');

// Initialize Materialize tabs
var options = {}; // Customize options as needed
M.Tabs.getInstance(el, options);

function toggleContent(headerId) {
    const content = document.getElementById(headerId);
    if (content) {
        content.style.maxWidth === '10px' ? content.style.removeProperty('max-width') : content.style.maxWidth = '10px'; // Set your desired style
    } else {
        console.error(`Element with ID '${headerId}' not found.`);
    }
}


document.addEventListener("DOMContentLoaded", function(){
    //....
    M.Tabs.init(el[0], options);
    function loadthwidth(){
        theads = document.getElementsByTagName('th')
        for (const th of theads) {
            th.style.maxWidth = '10px';
        }
    }
    loadthwidth()
});
