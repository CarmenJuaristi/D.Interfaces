package com.example.myothercatalog;

import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;
import android.content.Intent;

import androidx.appcompat.app.AppCompatActivity;

public class DetailActivity  extends AppCompatActivity {
    //Creamos la clase para el botón pueda funcionar
    private TextView nombre;
    private ImageView imagen;
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);
        Intent intent = getIntent();
        String textView = intent.getStringExtra("textView");
        String imageView = intent.getStringExtra("imageView");
        nombre = findViewById(R.id.name);
        imagen = findViewById(R.id.imagen);
        nombre.setText(textView);
        Util.downloadBitmapToImageView(imageView, this.imagen);



    }

}
