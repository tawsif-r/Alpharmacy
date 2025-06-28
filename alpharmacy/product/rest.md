###
- http request

```http
###

POST http://localhost:8003/product/api/products HTTP/1.1
content-type: application/json

{
    "name": "sample",
    "created_at": "Wed, 21 Oct 2015 18:27:50 GMT"
}
```


k8s/
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── db-deployment.yaml
│   ├── db-service.yaml
│   └── configmap.yaml