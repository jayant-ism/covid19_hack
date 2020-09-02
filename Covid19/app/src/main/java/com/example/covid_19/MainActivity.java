package com.example.covid_19;

import android.app.ProgressDialog;
import android.content.Intent;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.Toast;

import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.material.bottomnavigation.BottomNavigationView;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.OnProgressListener;
import com.google.firebase.storage.StorageReference;
import com.google.firebase.storage.UploadTask;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.ui.AppBarConfiguration;
import androidx.navigation.ui.NavigationUI;

import java.io.IOException;
import java.util.UUID;

import static android.view.View.X;
import static androidx.core.content.ContextCompat.startActivity;

public class MainActivity extends AppCompatActivity {

    private Button chooser;
    private ImageView imageview;
    private Uri filepath;
    private FirebaseStorage storage;
    private StorageReference storageReference;
    


    @Override
    protected void onCreate(Bundle savedInstanceState) {
       super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        BottomNavigationView navView = findViewById(R.id.nav_view);
        // Passing each menu ID as a set of Ids because each
        // menu should be considered as top level destinations.
        AppBarConfiguration appBarConfiguration = new AppBarConfiguration.Builder(
                R.id.navigation_home, R.id.navigation_dashboard)
                .build();
        NavController navController = Navigation.findNavController(this, R.id.nav_host_fragment);
        NavigationUI.setupActionBarWithNavController(this, navController, appBarConfiguration);
        NavigationUI.setupWithNavController(navView, navController);



       // chooser = (Button) findViewById(R.id.choose);
        imageview =(ImageView) findViewById(R.id.img);


        
    }

    public void chooser(View view)
    {
        chooseimage();
    }
    private void chooseimage() {
        Intent intent =new Intent();
        intent.setType("image/*");
        intent.setAction(Intent.ACTION_GET_CONTENT);
        startActivityForResult(Intent.createChooser(intent,"Select Image"),1);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if(requestCode == 1 && resultCode == RESULT_OK  && data!=null && data.getData()!=null)
        {
            filepath = data.getData();
           // Bundle extras = data.getExtras();
           // Bitmap bitmap = (Bitmap) extras.get("data");

            imageview =(ImageView) findViewById(R.id.img);
           // imageview.setImageResource(R.drawable.common_google_signin_btn_icon_dark_normal);

            try {
                //Bitmap photo = (Bitmap) data.getExtras().get("data");
                Bitmap bitmap = MediaStore.Images.Media.getBitmap(getContentResolver(), filepath);
                imageview.setImageBitmap(bitmap);
            } catch (IOException e) {
              e.printStackTrace();

            }
        }

    }
public void uploader(View view)
{
    uploadImage();

}
    public  void locator(View view){
        startActivity(new Intent(this, MapsActivity.class));

    }

    private void uploadImage() {

        storage = FirebaseStorage.getInstance();
        storageReference = storage.getReference();

        if(filepath != null)
        {
            final ProgressDialog progressdialog = new ProgressDialog(this);
            progressdialog.setTitle("Uploading");
            progressdialog.show();
            StorageReference refernce = storageReference.child("images/"+ UUID.randomUUID().toString());

            refernce.putFile(filepath)
                    .addOnSuccessListener(new OnSuccessListener<UploadTask.TaskSnapshot>() {
                        @Override
                        public void onSuccess(UploadTask.TaskSnapshot taskSnapshot) {
                            Toast.makeText(MainActivity.this, "Image Uploaded", Toast.LENGTH_SHORT).show();
                            progressdialog.dismiss();
                        }
                    })
                    .addOnProgressListener(new OnProgressListener<UploadTask.TaskSnapshot>() {
                        @Override
                        public void onProgress(UploadTask.TaskSnapshot taskSnapshot) {
                            double progress = (100.0*taskSnapshot.getBytesTransferred()/taskSnapshot.getTotalByteCount());
                            progressdialog.setMessage(("Uploaded" + (int)progress + "%"));
                        }
                    });
        }
    }
   /*private void uploadImage()
   {

       storage = FirebaseStorage.getInstance();
       storageReference = storage.getReference();
       if (filepath != null) {

           // Code for showing progressDialog while uploading
           final ProgressDialog progressDialog
                   = new ProgressDialog(this);
           progressDialog.setTitle("Uploading...");
           progressDialog.show();

           // Defining the child of storageReference
           StorageReference ref
                   = storageReference
                   .child(
                           "images/"
                                   + UUID.randomUUID().toString());

           // adding listeners on upload
           // or failure of image
           ref.putFile(filepath)
                   .addOnSuccessListener(
                           new OnSuccessListener<UploadTask.TaskSnapshot>() {

                               @Override
                               public void onSuccess(
                                       UploadTask.TaskSnapshot taskSnapshot)
                               {

                                   // Image uploaded successfully
                                   // Dismiss dialog
                                   progressDialog.dismiss();
                                   Toast
                                           .makeText(MainActivity.this,
                                                   "Image Uploaded!!",
                                                   Toast.LENGTH_SHORT)
                                           .show();
                               }
                           })

                   .addOnFailureListener(new OnFailureListener() {
                       @Override
                       public void onFailure(@NonNull Exception e)
                       {

                           // Error, Image not uploaded
                           progressDialog.dismiss();
                           Toast
                                   .makeText(MainActivity.this,
                                           "Failed " + e.getMessage(),
                                           Toast.LENGTH_SHORT)
                                   .show();
                       }
                   })
                   .addOnProgressListener(
                           new OnProgressListener<UploadTask.TaskSnapshot>() {

                               // Progress Listener for loading
                               // percentage on the dialog box
                               @Override
                               public void onProgress(
                                       UploadTask.TaskSnapshot taskSnapshot)
                               {
                                   double progress
                                           = (100.0
                                           * taskSnapshot.getBytesTransferred()
                                           / taskSnapshot.getTotalByteCount());
                                   progressDialog.setMessage(
                                           "Uploaded "
                                                   + (int)progress + "%");
                               }
                           });
       }
   }*/
}


