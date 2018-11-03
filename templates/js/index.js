var _slicedToArray = function () {function sliceIterator(arr, i) {var _arr = [];var _n = true;var _d = false;var _e = undefined;try {for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) {_arr.push(_s.value);if (i && _arr.length === i) break;}} catch (err) {_d = true;_e = err;} finally {try {if (!_n && _i["return"]) _i["return"]();} finally {if (_d) throw _e;}}return _arr;}return function (arr, i) {if (Array.isArray(arr)) {return arr;} else if (Symbol.iterator in Object(arr)) {return sliceIterator(arr, i);} else {throw new TypeError("Invalid attempt to destructure non-iterable instance");}};}();var _createClass = function () {function defineProperties(target, props) {for (var i = 0; i < props.length; i++) {var descriptor = props[i];descriptor.enumerable = descriptor.enumerable || false;descriptor.configurable = true;if ("value" in descriptor) descriptor.writable = true;Object.defineProperty(target, descriptor.key, descriptor);}}return function (Constructor, protoProps, staticProps) {if (protoProps) defineProperties(Constructor.prototype, protoProps);if (staticProps) defineProperties(Constructor, staticProps);return Constructor;};}();function _classCallCheck(instance, Constructor) {if (!(instance instanceof Constructor)) {throw new TypeError("Cannot call a class as a function");}}var MAIN_IMAGE_URL = 'https://image.ibb.co/mq8V3A/web.jpg';
var MOSAIC_IMAGE_URL = 'https://image.ibb.co/eJfgOA/Mosaic-min.jpg';

var Utils = {
  groupByArray: function groupByArray(xs, key) {
    return xs.reduce(function (rv, x) {
      var v = key instanceof Function ? key(x) : x[key];
      var el = rv.find(function (r) {return r && r.key === v;});
      if (el) {
        el.values.push(x);
      } else {
        rv.push({ key: v, values: [x] });
      }
      return rv;
    }, []);
  },
  getSizeToCover: function getSizeToCover(width, height, maxWidth, maxHeight) {
    var ratio = Math.max(maxWidth / width, maxHeight / height);
    return [width * ratio, height * ratio];
  },
  visibleHeightAtZDepth: function visibleHeightAtZDepth(camera) {var depth = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : 0;
    // compensate for cameras not positioned at z=0
    var cameraOffset = camera.position.z;
    if (depth < cameraOffset) depth -= cameraOffset;else
    depth += cameraOffset;

    // vertical fov in radians
    var vFOV = camera.fov * Math.PI / 180;

    // Math.abs to ensure the result is always positive
    return 2 * Math.tan(vFOV / 2) * Math.abs(depth);
  },
  visibleWidthAtZDepth: function visibleWidthAtZDepth(camera) {var depth = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : 0;
    var height = this.visibleHeightAtZDepth(camera, depth);
    return height * camera.aspect;
  } };var


SpriteTexture = function () {
  function SpriteTexture(texture, tilesHorizontal, tilesVertical, frameCount, frameNum) {_classCallCheck(this, SpriteTexture);
    this.texture = texture;
    this.tiles = { x: tilesHorizontal, y: tilesVertical };
    this.frameCount = frameCount;
    texture.wrapS = texture.wrapT = THREE.RepeatWrapping;
    texture.repeat.set(1 / this.tiles.x, 1 / this.tiles.y);
    this.setFrame(frameNum);
  }_createClass(SpriteTexture, [{ key: 'setFrame', value: function setFrame(

    frameIndex) {
      var xIndex = frameIndex % this.tiles.x;
      var yIndex = Math.floor(frameIndex / this.tiles.x);
      var halfX = 1 / this.tiles.x / 2;
      var halfY = 1 / this.tiles.y / 2;
      this.texture.offset.x = xIndex / this.tiles.x + halfX;
      this.texture.offset.y = -(yIndex / this.tiles.y) - halfY;
    } }]);return SpriteTexture;}();var


Object3DResizer = function () {
  function Object3DResizer(camera, obj) {_classCallCheck(this, Object3DResizer);
    this.camera = camera;
    this.obj = obj;
    this.scale = new THREE.Vector2(1, 1);
    this.setSize(1, 1);
  }_createClass(Object3DResizer, [{ key: 'setSize', value: function setSize(

    width, height) {
      this.scale.set(width, height);
      this.update();
    } }, { key: 'update', value: function update()

    {var
      obj = this.obj,camera = this.camera,scale = this.scale;
      var w = Utils.visibleWidthAtZDepth(camera);
      var h = Utils.visibleHeightAtZDepth(camera);
      obj.scale.x = w * scale.x;
      obj.scale.y = h * scale.y;
    } }]);return Object3DResizer;}();var


TextureResizer = function () {
  function TextureResizer(texture, obj) {_classCallCheck(this, TextureResizer);
    this.obj = obj;
    this.texture = texture;
    this.texture.center.set(0.5, 0.5);
    this.texture.wrapS = this.texture.wrapT = THREE.ClampToEdgeWrapping;
    this.scale = new THREE.Vector2(1, 1);
    this.originalSize = new THREE.Vector2(1, 1);
  }_createClass(TextureResizer, [{ key: 'updateTextureSize', value: function updateTextureSize()

    {var
      originalSize = this.originalSize,texture = this.texture;var _texture$image =
      texture.image,nW = _texture$image.naturalWidth,nH = _texture$image.naturalHeight;
      if (nW > nH) {
        originalSize.x = 1;
        originalSize.y = nH / nW;
      } else {
        originalSize.x = nW / nH;
        originalSize.y = 1;
      }
    } }, { key: 'update', value: function update()

    {var
      scale = this.scale,texture = this.texture,obj = this.obj,originalSize = this.originalSize;
      var formFactorX = 1;
      var formFactorY = 1;

      /* 
                             get formFactor to cover the obj with texture while
                             keeping the original image ratio
                           */
      if (texture.image) {
        this.updateTextureSize();var _Utils$getSizeToCover =
        Utils.getSizeToCover(
        originalSize.x,
        originalSize.y,
        obj.scale.x,
        obj.scale.y),_Utils$getSizeToCover2 = _slicedToArray(_Utils$getSizeToCover, 2),widthCover = _Utils$getSizeToCover2[0],heightCover = _Utils$getSizeToCover2[1];

        formFactorX = widthCover / obj.scale.x;
        formFactorY = heightCover / obj.scale.y;

      }
      var scaleX = 1 / (this.scale.x * formFactorX);
      var scaleY = 1 / (this.scale.y * formFactorY);
      texture.repeat.set(scaleX, scaleY);

    } }]);return TextureResizer;}();var


ImagePlane = function () {
  function ImagePlane(textureUrl, camera) {_classCallCheck(this, ImagePlane);
    this.scale = new THREE.Vector2(1, 1);
    this.texture = new THREE.TextureLoader().load(textureUrl, this.updateSize.bind(this));
    this.geometry = new THREE.PlaneBufferGeometry(1, 1, 1, 1);
    this.material = new THREE.MeshLambertMaterial({
      map: this.texture,
      wireframe: false });

    this.mesh = new THREE.Mesh(this.geometry, this.material);
    this.objectResizer = new Object3DResizer(camera, this.mesh);
    this.textureResizer = new TextureResizer(this.texture, this.mesh);
  }_createClass(ImagePlane, [{ key: 'updateSize', value: function updateSize()

    {
      this.objectResizer.scale.copy(this.scale);
      this.objectResizer.update();
      this.textureResizer.update();
    } }]);return ImagePlane;}();var


HexGrid = function () {
  function HexGrid(camera) {_classCallCheck(this, HexGrid);
    this.lastActiveCell = undefined;
    this.activeCells = [];
    this.groupObject = new THREE.Object3D();
    this.texture = new THREE.Texture();
    this.camera = camera;
    this.initLayout();
    this.initGrid();
  }_createClass(HexGrid, [{ key: 'getTileMaterial', value: function getTileMaterial(

    overlay, frameIndex) {
      var framesCount = 64;
      var tilesX = 8;
      var tilesY = 8;
      var halfX = 1 / tilesX / 2;
      var halfY = 1 / tilesY / 2;
      frameIndex = frameIndex % framesCount;
      var xIndex = frameIndex % tilesX;
      var yIndex = Math.floor(frameIndex / tilesX);
      var x = 1 - xIndex / tilesX - halfX;
      var y = 1 - yIndex / tilesY - halfY;

      var uniforms = {
        texture: { type: 't', value: this.texture },
        offset: { type: 'v2', value: new THREE.Vector2(x, y) },
        repeat: { type: 'v2', value: new THREE.Vector2(1 / tilesX, 1 / tilesY) },
        opacity: { type: 'f', value: 1 },
        color: { type: 'c', value: new THREE.Color(0xffffff) } };


      var fragSelector = overlay ? '#shader-texture-overlay-fragment' : '#shader-texture-normal-fragment';
      var fragShaderContent = document.querySelector(fragSelector).textContent;
      var vertexShaderContent = document.querySelector('#shader-texture-vertex').textContent;

      var mat = new THREE.ShaderMaterial({
        uniforms: uniforms,
        vertexShader: vertexShaderContent,
        fragmentShader: fragShaderContent,
        transparent: true
        //wireframe: true
      });

      if (overlay) {
        mat.blending = THREE.CustomBlending;
        mat.blendSrc = THREE.SrcColorFactor;
        mat.blendDst = THREE.DstColorFactor;
        mat.blendEquation = THREE.AddEquation;
      }

      mat.offset = mat.uniforms.offset.value;
      mat.repeat = mat.uniforms.repeat.value;
      mat.color = mat.uniforms.color.value;

      return mat;
    } }, { key: 'getMeshFromCell', value: function getMeshFromCell(

    cell, overlayMaterial, frameIndex) {var
      gridLayout = this.gridLayout;
      var mat = this.getTileMaterial(overlayMaterial, frameIndex);
      var mesh = new THREE.Mesh(gridLayout.cellShapeGeo, mat);
      mesh.position.copy(gridLayout.cellToPixel(cell));
      mesh.rotateOnAxis(new THREE.Vector3(1, 0, 0), Math.PI / 2);
      mesh.scale.set(0.96, 0.96, 1);
      mesh.userData.cell = cell;
      mesh.userData.frameIndex = frameIndex;
      return mesh;
    } }, { key: 'initGrid', value: function initGrid()

    {var _this = this;var
      texture = this.texture,groupObject = this.groupObject,gridLayout = this.gridLayout;
      var cellKeys = Object.keys(gridLayout.cells);
      cellKeys.forEach(function (k, frameIndex) {
        var cell = gridLayout.cells[k];
        var mesh = _this.getMeshFromCell(cell, true, frameIndex);
        mesh.userData.isOver = false;
        groupObject.add(mesh);
      });

      groupObject.rotation.x = -Math.PI / 2;
      groupObject.position.z = 2.5;
    } }, { key: 'setTexture', value: function setTexture(

    textureUrl) {var _this2 = this;
      this.texture = new THREE.TextureLoader().load(textureUrl, this.updateSize.bind(this));
      this.groupObject.children.forEach(function (c) {return c.material.uniforms.texture.value = _this2.texture;});
    } }, { key: 'initLayout', value: function initLayout()

    {
      this.gridLayout = new vg.HexGrid({ cellSize: 0.45 });
      this.gridLayout.generate({ size: 8 });
    } }, { key: 'updateSize', value: function updateSize()

    {
      var h = Utils.visibleHeightAtZDepth(this.camera, 1.5);
      var w = Utils.visibleWidthAtZDepth(this.camera, 1.5);
      var aspect = w / h;
      var gridSize = 16 * 0.55;
      this.groupObject.scale.set(w / gridSize, 1, h / gridSize * aspect);
    } }, { key: 'animateHoverTileIn', value: function animateHoverTileIn(

    mesh) {
      var tl = new TimelineMax();
      mesh.material.uniforms.opacity.value = 0;
      tl.to(mesh.material.uniforms.opacity, 0.5, { value: 0.8 });
      tl.to(mesh.scale, 0.35, { x: 1, y: 1 }, -0.5);

    } }, { key: 'animateHoverTileOut', value: function animateHoverTileOut(

    mesh) {var _this3 = this;
      var tl = new TimelineMax({ onComplete: function onComplete() {
          _this3.groupObject.remove(mesh);
          mesh.geometry.dispose();
          mesh.material.dispose();
          mesh = undefined;
        } });

      tl.to(mesh.material.uniforms.opacity, 0.95, {
        value: 0 });

    } }, { key: 'animateGridTilesIn', value: function animateGridTilesIn()


    {

      var tiles = this.groupObject.children.map(function (c) {
        var cell = c.userData.cell;
        var d = Math.max(Math.abs(cell.q), Math.abs(cell.r), Math.abs(cell.s));
        return { target: c, d: d };
      });

      var rings = Utils.groupByArray(tiles, 'd');
      rings.forEach(function (r) {
        r.values.forEach(function (item) {
          var target = item.target;
          target.scale.set(0.5, 0.5, 1);
          TweenMax.to(target.scale, item.d * 0.22 + 0.8, {
            x: 0.96,
            y: 0.96,
            ease: Power3.easeOut,
            delay: item.d * 0.12 });

        });
      });

      TweenMax.from(this.groupObject.position, 2, {
        z: 7,
        ease: Power3.easeOut });

    } }, { key: 'deactivateAll', value: function deactivateAll()

    {
      while (this.activeCells.length > 0) {
        var c = this.activeCells.pop();
        this.animateHoverTileOut(c);
      }
    } }, { key: 'setActiveCell', value: function setActiveCell(

    object3d) {
      if (object3d && object3d.userData.isOver === false) {
        if (this.lastActiveCell != object3d) {
          this.deactivateAll();
          this.lastActiveCell = object3d;
          var mat = this.getTileMaterial(false, 1);
          var mesh = this.getMeshFromCell(object3d.userData.cell, false, object3d.userData.frameIndex);
          mesh.userData.isOver = true;
          mesh.position.y = 0.99;
          this.animateHoverTileIn(mesh);
          this.activeCells.push(mesh);
          this.groupObject.add(mesh);
        }
      }
    } }]);return HexGrid;}();var


App = function () {
  function App() {var _this4 = this;_classCallCheck(this, App);
    this.width = 0;
    this.height = 0;
    this.mouse = new THREE.Vector2(0, 0);
    this.raycaster = new THREE.Raycaster();
    this.init();
    //this.initOrbitControls();
    this.setupScene();
    this.setupLights();
    this.attachEvents();
    this.setupMosaic();
    this.onResize();
    this.onFrame(0);
    this.loader = THREE.DefaultLoadingManager;
    this.loader.onProgress = function (url, itemsLoaded, itemsTotal) {
      if (itemsLoaded === itemsTotal) {
        _this4.mosaicAnimationIn();
      }
    };
  }_createClass(App, [{ key: 'init', value: function init()

    {var _window =
      window,w = _window.innerWidth,h = _window.innerHeight;
      this.renderer = new THREE.WebGLRenderer({
        antialias: true });

      this.scene = new THREE.Scene();
      this.camera = new THREE.PerspectiveCamera(45, 0, 0.1, 1000);
      this.renderer.setPixelRatio(window.devicePixelRatio);
      this.clock = new THREE.Clock();
      document.body.appendChild(this.renderer.domElement);
    } }, { key: 'initOrbitControls', value: function initOrbitControls()

    {
      var c = new THREE.OrbitControls(this.camera, this.renderer.domElement);
      c.enableDamping = true;
      c.dampingFactor = 0.25;
      c.minDistance = 1;
      c.maxDistance = 100;
      this.orbitControls = c;
    } }, { key: 'attachEvents', value: function attachEvents()

    {
      window.addEventListener("resize", this.onResize.bind(this));
      window.addEventListener("mousemove", this.onMouseMove.bind(this));
    } }, { key: 'onMouseMove', value: function onMouseMove(

    event) {
      this.mouse.x = event.clientX / window.innerWidth * 2 - 1;
      this.mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
    } }, { key: 'onResize', value: function onResize()

    {
      this.resize();
      this.background.updateSize();
      this.grid.updateSize();
    } }, { key: 'resize', value: function resize()

    {var
      renderer = this.renderer,camera = this.camera;var _window2 =
      window,w = _window2.innerWidth,h = _window2.innerHeight;
      renderer.setSize(w, h);
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      this.width = w;
      this.height = h;
    } }, { key: 'setupScene', value: function setupScene()

    {var
      scene = this.scene;
      scene.background = new THREE.Color(0xffffff);
      this.camera.position.z = 10;
    } }, { key: 'setupLights', value: function setupLights()

    {var
      scene = this.scene;
      var light = new THREE.AmbientLight(0xffffff);
      this.pLight = new THREE.PointLight(0xffffff, 1, 20);
      this.pLight.position.set(0, 0, 9);
      scene.add(this.pLight);
      scene.add(light);
    } }, { key: 'setupMosaic', value: function setupMosaic()

    {var
      scene = this.scene,camera = this.camera;
      this.background = new ImagePlane(MAIN_IMAGE_URL, camera);
      this.background.scale.set(1.1, 1.1, 1);
      this.grid = new HexGrid(camera);
      this.grid.setTexture(MOSAIC_IMAGE_URL);
    } }, { key: 'updateGridOver', value: function updateGridOver()

    {var
      camera = this.camera,raycaster = this.raycaster,mouse = this.mouse,grid = this.grid;
      if (mouse.x !== 0 && mouse.y !== 0) {
        raycaster.setFromCamera(mouse, camera);
        var intersects = raycaster.intersectObjects(this.grid.groupObject.children);
        if (intersects.length) {
          grid.setActiveCell(intersects[0].object);
        }
      }
    } }, { key: 'mosaicAnimationIn', value: function mosaicAnimationIn()

    {var _this5 = this;var
      scene = this.scene;
      scene.add(this.background.mesh);
      scene.add(this.grid.groupObject);
      this.grid.animateGridTilesIn();

      TweenMax.to(this.pLight, 1.5, {
        intensity: 0 });


      TweenMax.from(this.background.scale, 1.8, {
        x: 1.4,
        y: 1.4,
        onUpdate: function onUpdate() {
          _this5.background.updateSize();
        },
        ease: Power4.easeOut });

    } }, { key: 'updateMosaicTilt', value: function updateMosaicTilt()

    {var
      camera = this.camera,mouse = this.mouse;
      TweenMax.to(this.camera.position, 1.5, {
        x: mouse.x * 0.5,
        y: mouse.y * 0.5 });

    } }, { key: 'onFrame', value: function onFrame(

    time) {var
      renderer = this.renderer,scene = this.scene,camera = this.camera,clock = this.clock;
      requestAnimationFrame(this.onFrame.bind(this));
      //this.orbitControls.update();
      this.updateGridOver();
      this.updateMosaicTilt();
      camera.lookAt(scene.position);
      renderer.render(scene, camera);
    } }]);return App;}();


window.app = new App();