function lineintersects (p0, p1, p2, p3) {
  var s1x, s1y, s2x, s2y
  s1x = p1['x'] - p0['x']
  s1y = p1['y'] - p0['y']
  s2x = p3['x'] - p2['x']
  s2y = p3['y'] - p2['y']

  var s, t
  s = (-s1y * (p0['x'] - p2['x']) + s1x * (p0['y'] - p2['y'])) / (-s2x * s1y + s1x * s2y)
  t = (s2x * (p0['y'] - p2['y']) - s2y * (p0['x'] - p2['x'])) / (-s2x * s1y + s1x * s2y)

  if (s >= 0 && s <= 1 && t >= 0 && t <= 1) {
    // Collision detected
    return true
  }
  return false // No collision
}

const checkIntersect = function (x, y, perimeter) {
  if (perimeter.length < 4) {
    return false
  }
  let p0 = []
  let p1 = []
  let p2 = []
  let p3 = []

  p2['x'] = perimeter[perimeter.length - 1]['x']
  p2['y'] = perimeter[perimeter.length - 1]['y']
  p3['x'] = x
  p3['y'] = y

  for (var i = 0; i < perimeter.length - 1; i++) {
    p0['x'] = perimeter[i]['x']
    p0['y'] = perimeter[i]['y']
    p1['x'] = perimeter[i + 1]['x']
    p1['y'] = perimeter[i + 1]['y']
    if (p1['x'] === p2['x'] && p1['y'] === p2['y']) { continue }
    if (p0['x'] === p3['x'] && p0['y'] === p3['y']) { continue }
    if (lineintersects(p0, p1, p2, p3) === true) {
      return true
    }
  }
  return false
}

export default { checkIntersect }
