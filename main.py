from fastapi import FastAPI
from app.routes.issues import router
from fastapi.middleware.cors import CORSMiddleware
# create an instance of FastAPI
app = FastAPI()

# add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)



app.include_router(router)


# # # create another endpoint
# # @app.get("/hello/{name}")
# # def greet(name: str):
# #     return {"message": f"Hello {name}, welcome to FastAPI isolation learning!"}




# from fastapi import FastAPI, HTTPException

# app = FastAPI()

# gadgets = [
#     {"id": 1, "name": "iPhone 15", "brand": "Apple", "price": 1000, "category": "Mobile"},
#     {"id": 2, "name": "Galaxy S24", "brand": "Samsung", "price": 900, "category": "Mobile"},
#     {"id": 3, "name": "MacBook Air", "brand": "Apple", "price": 1200, "category": "Laptop"},
#     {"id": 4, "name": "Pixel 8", "brand": "Google", "price": 700, "category": "Mobile"},
#     {"id": 5, "name": "Dell XPS 13", "brand": "Dell", "price": 1100, "category": "Laptop"},
#     {"id": 6, "name": "iPad Pro", "brand": "Apple", "price": 800, "category": "Tablet"},
#     {"id": 7, "name": "Surface Pro", "brand": "Microsoft", "price": 950, "category": "Tablet"},
#     {"id": 8, "name": "Sony WH-1000XM5", "brand": "Sony", "price": 350, "category": "Audio"},
#     {"id": 9, "name": "AirPods Pro", "brand": "Apple", "price": 250, "category": "Audio"},
#     {"id": 10, "name": "Logitech MX Master", "brand": "Logitech", "price": 100, "category": "Accessories"},
# ]
# @app.get("/gadgets")
# def get_gadgets(category: str = None, min_price: int = 0):
#     filtered_data = gadgets
#     if category:
#         filtered_data =[g for g in filtered_data if g["category"].lower() == category.lower()]
    
#     if min_price:
#         filtered_data = [g for g in filtered_data if g["price"] >= min_price]
        
#     print(f"Filter used - Category: {category}, Min Price: {min_price}")
#     return filtered_data


# # get by a single id
# @app.get("/gadgets/{g_id}")
# def get_single_gadget(g_id: int):
#     for g in gadgets:
#         if g["id"] == g_id:
#             return g
#     raise HTTPException(status_code=404, detail="Gadget not found")

