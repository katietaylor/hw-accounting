SALESPERSON_INDEX = 0
INTERNET_INDEX = 1
DORKY_LINE_LENGTH = 80

print "*" * DORKY_LINE_LENGTH


def order_tallies(order_type_file):
    """ Open file and tally the orders by type
    """

    orders = open(order_type_file)

    melon_tallies = {
        "Musk": 0,
        "Hybrid": 0,
        "Watermelon": 0,
        "Winter": 0
        }

    for line in orders:
        data = line.split("|")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count

    orders.close()

    return melon_tallies


def melon_revenue(melon_tallies):
    """calculate revenue
    """

    melon_prices = {
        "Musk": 1.15,
        "Hybrid": 1.30,
        "Watermelon": 1.75,
        "Winter": 4.00
        }

    total_revenue = 0

    print "MELON SALES DATA"

    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue

        print "We sold {} {} melons at {:.2f} each for a total of {:.2f}" .format(
            melon_tallies[melon_type], melon_type, price, revenue)


def sales_team_performance(sales_file):
    """ Calculate and compare sales team to online sales.
    """

    sales_type = open(sales_file)
    sales_team = 0
    online = 0

    for line in sales_type:
        data = line.split("|")
        if data[1] == "0":
            online += float(data[3])
        else:
            sales_team += float(data[3])
    print "SALES TYPE DATA"
    print "Salespeople generated ${:.2f} in revenue.".format(sales_team)
    print "Internet sales generated ${:.2f} in revenue.".format(online)
    if sales_team > online:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"


melon_tallies = order_tallies("orders-by-type.txt")
melon_revenue(melon_tallies)
sales_team_performance("orders-with-sales.txt")
