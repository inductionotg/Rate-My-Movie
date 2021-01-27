#End Points   
   ##Register
   
   
        * Registration for the user
	    * Url
	
	        * http://127.0.0.1:8000/api/auth/register
	    * Method
            * Post
        
	Success Response
	
    {"user":{"id":21,"username":"hp1","email":"rit@gmail.com"},"token":"53b5c7208b5a15a22879655d9eec685661ca1bee95bac901b6a2d436dcdfb6aa"}
2.Login

    login for user
    
    Url
        http://127.0.0.1:8000/api/auth/login
    Method
        POST
    Success Response
    
        {"user":{"id":21,"username":"hp1","email":"rit@gmail.com"},"token":"a4c5c1f43267d50a66dae373639290ceefa8d737830825689054f103fca88f78"}
3.Movie

    add the title and director
    
    url
        http://127.0.0.1:8000/api/auth/movies
    Method
        POST
        GET
    sucess response
     Post- {"id":37,"title":"Transformer","director":"XYZ"}
     Get-   {
            "id": 36,
            "title": "Transformer",
            "director": "XYZ"
        },
        {
            "id": 37,
            "title": "Transformer",
            "director": "XYZ"
        }
    ]
4.Rating

    add ratings
    
    Url
        http://127.0.0.1:8000/api/auth/rating
    Method
        GET
        POST
    Sucess Response
        Post-{"detail":"You cant rate it "}
        Get-{
            "id": 15,
            "movie": 6,
            "rating": 2
        },
        {
            "id": 16,
            "movie": 6,
            "rating": 2
        },
    
        {
            "id": 17,
            "movie": 3,
            "rating": 4
        },
5.Logout

    Url
    
        http://127.0.0.1:8000/api/auth/logout
     
    Method
        POST
        
    Sucess Response 
        
        204 No content
   