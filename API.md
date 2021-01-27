#End Points   
 ##Register
   - Registration for the user
	    * Url
	        * http://127.0.0.1:8000/api/auth/register
	    * Method
            * Post
        
        * Success Response
        
                json         
	
                {
                "user":{
                "id":21,
                "username":"hp1",
                "email":"rit@gmail.com"
                },
                "token":"53b5c7208b5a15a22879655d9eec685661ca1bee95bac901b6a2d436dcdfb6aa"
                }
            
   - Login

     **login for user**
    
        - Url
            * http://127.0.0.1:8000/api/auth/login
        - Method
        
            - POST
        - Success Response
                    
                    
                    json
                    
                    {
             
                    "user": {
                
                    "id": 21,
                   
                    "username": "hp1",
                   
                    "email": "rit@gmail.com"
                   
                        },
                        
                        "token": "847f06d4ec4458e4f2f8e3e219cd4b0871abf8723ccd0e53ef1f73219ea66da7"
                    }

- Movie

    **add the title and director**
    
     - url
        - http://127.0.0.1:8000/api/auth/movies
    - Method
        - POST
        - GET
    - sucess response
    
        1.Post
        
               JSON
                
               {
                "id":37,
                "title":"Transformer",
                "director":"XYZ"
               }
     
        2.Get  
            
                JSON
            {
                "id": 36,
                "title": "Transformer",
                "director": "XYZ"
            },
            {
                "id": 37,
                "title": "Transformer",
                "director": "XYZ"
            }
    
- Rating

    **add ratings**
    
    - Url
        - http://127.0.0.1:8000/api/auth/rating
    - Method
        - GET
        - POST
        
    - Sucess Response
        
        - Post
        
                JSON
        
                {
                "detail":"You cant rate it "
                }
        
         - Get
         
            json
         
         
            {
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
        
- Logout

    - Url
    
        - http://127.0.0.1:8000/api/auth/logout
     
    - Method
        - POST
        
    - Sucess Response 
        
        - 204 No content
   