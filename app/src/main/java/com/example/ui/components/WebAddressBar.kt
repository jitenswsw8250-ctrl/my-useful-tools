package com.example.ui.components

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.DarkMode
import androidx.compose.material.icons.filled.Home
import androidx.compose.material.icons.filled.LightMode
import androidx.compose.material.icons.filled.Menu
import androidx.compose.material.icons.filled.Share
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.model.Screen

@Composable
fun WebAddressBar(
  currentScreen: Screen,
  isDarkTheme: Boolean,
  onToggleTheme: () -> Unit,
  onNavigateHome: () -> Unit,
  onNavigateBack: () -> Unit,
  onOpenMenu: () -> Unit,
  canNavigateBack: Boolean,
  onNavigate: (Screen) -> Unit = {},
  modifier: Modifier = Modifier
) {
  val context = LocalContext.current

  Surface(
    modifier = modifier.fillMaxWidth(),
    color = MaterialTheme.colorScheme.surface,
    tonalElevation = 2.dp,
    shadowElevation = 2.dp
  ) {
    Column(
      modifier = Modifier
        .fillMaxWidth()
        .padding(horizontal = 12.dp, vertical = 6.dp)
    ) {
      // Top row: Brand & Primary Navigation Controls
      Row(
        modifier = Modifier.fillMaxWidth(),
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.SpaceBetween
      ) {
        // Left: Navigation & Branding
        Row(verticalAlignment = Alignment.CenterVertically) {
          if (canNavigateBack) {
            IconButton(
              onClick = onNavigateBack,
              modifier = Modifier
                .size(40.dp)
                .testTag("back_button")
            ) {
              Icon(
                imageVector = Icons.AutoMirrored.Filled.ArrowBack,
                contentDescription = "Back to Home",
                tint = MaterialTheme.colorScheme.onSurface
              )
            }
          } else {
            IconButton(
              onClick = onOpenMenu,
              modifier = Modifier
                .size(40.dp)
                .testTag("menu_button")
            ) {
              Icon(
                imageVector = Icons.Default.Menu,
                contentDescription = "Open Navigation Menu",
                tint = MaterialTheme.colorScheme.onSurface
              )
            }
          }

          Spacer(modifier = Modifier.width(4.dp))

          Text(
            text = "MY USEFUL TOOLS",
            style = MaterialTheme.typography.titleMedium,
            fontWeight = FontWeight.Black,
            letterSpacing = 0.5.sp,
            color = MaterialTheme.colorScheme.primary,
            modifier = Modifier.clickable { onNavigateHome() }
          )
        }

        // Right: Action controls (Home, Theme Toggle, Share)
        Row(verticalAlignment = Alignment.CenterVertically) {
          if (canNavigateBack) {
            IconButton(
              onClick = onNavigateHome,
              modifier = Modifier
                .size(40.dp)
                .testTag("home_button")
            ) {
              Icon(
                imageVector = Icons.Default.Home,
                contentDescription = "Go to Home",
                tint = MaterialTheme.colorScheme.onSurfaceVariant
              )
            }
          }

          IconButton(
            onClick = onToggleTheme,
            modifier = Modifier
              .size(40.dp)
              .testTag("theme_toggle_button")
          ) {
            Icon(
              imageVector = if (isDarkTheme) Icons.Default.LightMode else Icons.Default.DarkMode,
              contentDescription = "Toggle Light / Dark Mode",
              tint = MaterialTheme.colorScheme.onSurfaceVariant
            )
          }

          IconButton(
            onClick = {
              val sendIntent = android.content.Intent().apply {
                action = android.content.Intent.ACTION_SEND
                putExtra(
                  android.content.Intent.EXTRA_TEXT,
                  "Check out ${currentScreen.title} on MY USEFUL TOOLS: Free online utility calculators"
                )
                type = "text/plain"
              }
              context.startActivity(android.content.Intent.createChooser(sendIntent, "Share Tool"))
            },
            modifier = Modifier
              .size(40.dp)
              .testTag("share_button")
          ) {
            Icon(
              imageVector = Icons.Default.Share,
              contentDescription = "Share",
              tint = MaterialTheme.colorScheme.onSurfaceVariant
            )
          }
        }
      }
    }
  }
}
