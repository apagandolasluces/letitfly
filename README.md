# CS 160 uber project

# API endpoints

```
POST /rider/register            Rider Sign up
POST /driver/register           Driver Sign up
POST /rider/authenticate        Rider Sign in
POST /driver/authenticate       Driver Sign in
POST /resetpassword             Rider and Driver Reset password by email

POST /rider/request             Rider request a ride
POST /rider/cancel              Rider cancel ride

POST /rider/tip                 Rider pay tip

POST /driver/search             Driver search requests around me
POST /driver/accept             Driver choose a request
POST /driver/cancel             Driver cancel a pick up
POST /driver/pickup             Driver picked up the rider
POST /driver/track              Driver sends the current location
POST /driver/dropoff            Driver complete the pick up and arrived the rider's destination

POST /rider/logout              Rider log out
POST /driver/logout             Driver log out
```

# Details of each endpoint

## Register rider
Register a rider and save the rider's information into the database

* URL

  `/rider/register`

* Method

  `POST`

* Data Params

  ```JSON
  {
    rider: {
      email: "yuuki@yuuki.com",
      name: "Yuki Kuroshima",
      password: "password1234",
      creditCardInfo: {
        name: "Yuki Kuroshima",
        number: "1234545666",
        expireDate: "09/17",
        cvv: 333,
      },
    }
  }
  ```
 
* Success Response
  * Code: 201
  * Content
     ```
     { token: "Sample JSON Web Token" }
     ```

* Error Response
  * Code: 422
  * Content
     ```
     { error: "Email already taken" }
     or
     { error: "Credit card invalid" }
     ```

## Register driver
Register a driver and save the driver's information into the database

* URL

  `/driver/register`

* Method

  `POST`

* Data Params

  ```JSON
  {
    driver: {
      email: "yuuki@yuuki.com",
      name: "Yuki Kuroshima",
      password: "password1234",
      bankInfo: {
        routing: "1234556"
      },
    }
  }
  ```
 
* Success Response
  * Code: 201
  * Content
     ```
     { token: "Sample JSON Web Token" }
     ```

* Error Response
  * Code: 422
  * Content
     ```
     { error: "Email already taken" }
     or
     { error: "Bank information invalid" }
     ```

## Authenticate rider
Authenticate a rider who already have their account

* URL

  `/rider/authenticate`

* Method

  `POST`

* Data Params

  ```JSON
  {
    rider: {
      email: "yuuki@yuuki.com",
      password: "password1234",
    }
  }
  ```
 
* Success Response
  * Code: 200
  * Content
     ```
     { token: "Sample JSON Web Token" }
     ```

* Error Response
  * Code: 401 UNAUTHORIZED
  * Content
     ```
     { error: "Authentication failed" }
     ```

## Authenticate driver
Authenticate a driver who already have their account

* URL

  `/driver/authenticate`

* Method

  `POST`

* Data Params

  ```JSON
  {
    driver: {
      email: "yuuki@yuuki.com",
      password: "password1234",
    }
  }
  ```
 
* Success Response
  * Code: 200
  * Content
     ```
     { token: "Sample JSON Web Token" }
     ```

* Error Response
  * Code: 401 UNAUTHORIZED
  * Content
     ```
     { error: "Authentication failed" }
     ```

