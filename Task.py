from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    Browser=p.chromium.launch(headless=False)# Launch browser (headed mode)
    page=Browser.new_page()# Open a new browser page/tab
    page.goto("https://sauce-demo.myshopify.com/")# Open the home page
    
    # Select the product "Noir jacket"
    product=page.wait_for_selector("//h3[text()='Noir jacket']").click()# type:ignore
           
    # Click on "Add to Cart" Button    
    page.wait_for_selector('//input[@id="add"]').click()# type:ignore
    page.wait_for_timeout(3000)# Wait for cart update
    
    # Click on "Checkout" Preview  
    page.wait_for_selector('//a[text()="Check Out"]').click()# type:ignore
       
    # Verify product added in cart
    added_product_name=page.wait_for_selector('//a[text()="Noir jacket - S / Blue"]').is_visible()# type:ignore
    assert added_product_name,print("Product added successfully")# Assertion – Product added successfully
    
    # Click on My Cart option
    page.wait_for_selector('//a[text()="My Cart "]').click()# type:ignore
    
    # Click "Remove" Button to remove product
    page.wait_for_selector('//a[text()="Remove"]').click()# type:ignore
    
    # Verify cart is empty
    empty_cart=page.wait_for_selector('//p[text()="Your cart is empty."]').is_visible()# type:ignore
    assert empty_cart,print("Product removed successfully")# Assertion – Product removed successfully
    # Final wait
    page.wait_for_timeout(2000)
    
    Browser.close() # Close browser
    

    