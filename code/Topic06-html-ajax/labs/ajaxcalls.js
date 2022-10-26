
 
    function getAll(callback){
        $.ajax({
            "url": "http://andrewbeatty1.pythonanywhere.com/books",
            "method":"GET",
            "data":"",
            "dataType": "JSON",
            "success":function(result){
                //console.log(result);
                callback(result)
     
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }

    // testing code
    function createBook(book, callback){
        console.log(JSON.stringify(book));
        $.ajax({
            "url": "http://andrewbeatty1.pythonanywhere.com/books",
            "method":"POST",
            "data":JSON.stringify(book),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                //console.log(result);
                callback(result)  
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }
    function updateBook(book, callback){
        console.log("updateing " +JSON.stringify(book));
        $.ajax({
            "url": "http://andrewbeatty1.pythonanywhere.com/books/"+encodeURI(book.id),
            "method":"PUT",
            "data":JSON.stringify(book),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                console.log(result);
                callback(result)   
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
    }
    function deleteBook(id, callback){
        $.ajax({
            "url": "http://andrewbeatty1.pythonanywhere.com/books/"+id,
            "method":"DELETE",
            "data":"",
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                console.log(result);
                callback(result)  
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }



    // testing code
    
    function processGetAllResponse(result){
        console.log("in process")
        //console.log(result)
        for (book of result){
            //console.log(book)
            // issue the format of the book object is different from lab06.02
            // there are two solutions change the book object in lan06.02 to have capitals 
            // or convert
            displayBook = {}
            displayBook.id = book.id
            displayBook.author = book.Author
            displayBook.title = book.Title
            displayBook.price = book.Price
            // you can now pass it to addBookToTable
            console.log(displayBook)
        }
    }
     getAll(processGetAllResponse)

     ///// Create
    function processCreateResponse(result){
        console.log(result)
    }
    //book = {"Title":"javascript","Author":"andrew","Price":12} 
    //createBook(book,processCreateResponse) 

    //// update
    function processUpdateResponse(result){
        console.log(result)
    }
    book = {id:155,"Price":999} 
    //updateBook(book,processUpdateResponse)
    
    ////delete
    
    function processDeleteResponse(result){
        console.log("in pprocess delete")
        console.log(result)
    }
    //deleteBook(155,processUpdateResponse) 


