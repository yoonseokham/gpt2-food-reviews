# GPT2-food-reviews
[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/ha-mulan/gpt2-food-reviews)



### About

	it generates food reviews related to your input keyword.
	first, input your keyword
	second, wait for result

### How to use

	three ways to use Gpt2 recipe-maker
    	1.  CLI
    	2.  Swagger
    	3.  Demo

### GET parameter

    review: input your keyword than you will check out the food reviews related to keyword

### Output format

    generated text


##  *With CLI*

### Input example

    curl -X GET "https://main-gpt2-food-reviews-ha-mulan.endpoint.ainize.ai/api/?review=great" -H "accept: string"


### Output example

        great: I enjoy this tea. This tea is strong and flavorful and the taste was perfect for me. It did have a strange taste like peppermint but it wasn't overwhelming.

        Love it, love it.: I love Green Tea!! This has a great flavor, and very refreshing.  It's decaf and a wonderful anytime tea.  It's a must buy for me.

        This product is not for me.: The description of this product fails. Why? Because I hate Green Tea for some reason. I think people really need to know the fine print. I know that it says "Truly a Green Tea". This product is not for me. I don't consider myself a tea connoisseur but this product is not for me. I think a Green Tea drinker will like this product. Too bad because it's not for me.

        good tasting: Nice, smooth flavor, great blend of greens and spices. I will purchase again. Great product, one of my favorites.

        Tasty: This is by far the best green tea variety around.  It has a wonderful combination of spices and flavor.  A nice treat in the winter, or even during a summer break.

        nice stuff: I really like this.  It is not over powering and not overpowering.  I've made green tea latte's with a bit of this stuff and they were very very tasty.  I love the fact that it is organic



## *With swagger*

API page: [Ainize](https://ainize.ai/ha-mulan/gpt2-food-reviews?branch=main)

## *With a Demo*

Demo page: [End-point](https://main-gpt2-food-reviews-ha-mulan.endpoint.ainize.ai)
