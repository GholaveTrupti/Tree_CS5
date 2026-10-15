
import heapq

# City map: locations and road distances in km
city = {
    "Home": [("School", 4), ("Market", 2)],
    "School": [("Home", 4), ("Hospital", 5), ("Park", 3)],
    "Market": [("Home", 2), ("Park", 6)],
    "Park": [("Market", 6), ("School", 3), ("Hospital", 2)],
    "Hospital": [("School", 5), ("Park", 2)]
}

def shortest_path(start, end):
    distances = {place: float("inf") for place in city}
    distances[start] = 0
    previous = {}
    queue = [(0, start)]

    while queue:
        distance, current = heapq.heappop(queue)

        if distance > distances[current]:
            continue

        if current == end:
            break

        for neighbor, weight in city[current]:
            new_distance = distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current
                heapq.heappush(queue, (new_distance, neighbor))

    if distances[end] == float("inf"):
        print("No route found!")
        return

    path = []
    current = end

    while current != start:
        path.append(current)
        current = previous[current]

    path.append(start)
    path.reverse()

    print("\nShortest Route:", " -> ".join(path))
    print("Total Distance:", distances[end], "km")


print("Available Locations:", ", ".join(city))

start = input("Enter starting location: ").strip().title()
end = input("Enter destination: ").strip().title()

if start not in city or end not in city:
    print("Invalid location! Please choose from the list.")
elif start == end:
    print("Starting location and destination are the same.")
    print("Total Distance: 0 km")
else:
    shortest_path(start, end)
