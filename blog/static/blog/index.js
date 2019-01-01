

function updatePageForm() {
    document.querySelector('.blog-content').style.display = 'none';
    document.querySelector('#update_page_form').style.display = 'block'
}

function updatePostForm() {
    document.querySelector('.blog-content').style.display = 'none';
    document.querySelector('#update_post_form').style.display = 'block';
    let  blogdiv =  document.querySelector('.blog-div');
    blogdiv.style.display='none';
    // $('.form-title').insertAfter(title);
}
