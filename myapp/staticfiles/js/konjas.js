// сначала создаём контейнер
var stage = new Konva.Stage({
      container: 'container',  // индификатор div контейнера
      width: 500,
      height: 500
});

// далее создаём слой
var layer = new Konva.Layer();

// создаём фигуру
var circle = new Konva.Circle({
      x: stage.width() / 2,
      y: stage.height() / 2,
      radius: 70,
      fill: 'red',
      stroke: 'black',
      strokeWidth: 4
});

// добавляем круг на слой
layer.add(circle);

// добавляем слой
stage.add(layer);