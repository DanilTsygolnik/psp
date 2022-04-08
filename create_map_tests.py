chart_height = 1
chart_width = 1
cell_height = 1
cell_width = 1
correct_neighbors_set = set()
# map view (x - cell, * - cells on chart)
#   1 2
# 1 x *
# 1 * *
chart_height = 2
chart_width = 2
cell_height = 1
cell_width = 1
correct_neighbors_set = set(["h1w2","h2w1","h2w2"])

# map view (x - cell, * - cells on chart)
#   1 2 3
# 1 * * *
# 1 * x *
# 1 * * *
chart_height = 3
chart_width = 3
cell_height = 2
cell_width = 2
correct_neighbors_set = set(["h1w1","h1w2","h1w3",
                      "h2w1","h2w2","h2w3",
                      "h3w1","h3w2","h3w3"])
